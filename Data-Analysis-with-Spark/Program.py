import MongoDbConnectorClass as Mongo
import MsSQLConnectorClass as MsSQL
import Functions
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType, FloatType
from pyspark.sql import functions as f
import datetime
import json

## get the program start time to calculate process time
temptime = datetime.datetime.now()

## create a object of MongoDBConnection and Spark Session to get exist location packets from MongoDB database
mongoDB = Mongo.MongoDBConnection()
sparkSession = mongoDB.GetSparkSession()

## read all data from MongoDB and assisgn them into dataframe as df
df = sparkSession.read.format("mongo").load()

## specify the time which interval is when do you want to analysis datas
timeMax = datetime.datetime.now()
timeMin = datetime.datetime.now() - datetime.timedelta(days=30, hours=3, minutes=24)
timeMin = "2020-03-12 12:45:00.000"
timeMax = "2020-03-12 13:00:00.000"

## get time interval as min-max variable
timeMin = datetime.datetime.strptime("2020-03-12 12:15:00.000", '%Y-%m-%d %H:%M:%S.%f')
timeMax = datetime.datetime.strptime("2020-03-12 14:15:00.000", '%Y-%m-%d %H:%M:%S.%f')

## convert dataframe df to tempView to enable ask SQL queries.
df.createOrReplaceTempView("sqlMongo")

## specify the datetime interval and get all datas that are existed and order
packets = sparkSession.sql("select datetime,cast(positionX as float),cast(positionY as float),cast(linearX as float),cast(linearY as float),cast(rbt_id as int) from sqlMongo where datetime between '" + str(timeMin) + "' and '" + str(timeMax) + "' order by datetime").collect()

## show exist schema
# df.printSchema()

# Create a schema for the convert selected data list to dataframe
schema_Selected = StructType([
    StructField('datetime', StringType(), True),
    StructField('positionX', FloatType(), True),
    StructField('positionY', FloatType(), True),
    StructField('lineerX', FloatType(), True),
    StructField('lineerY', FloatType(), True),
    StructField('rbt_id', IntegerType(), True),
    StructField('tourCount', IntegerType(), True),
    StructField('wayID', StringType(), True),
    StructField('wayLength', FloatType(), True),
    StructField('rbtLength', FloatType(), True),
    StructField('action', IntegerType(), True)

])

# Create a schema for the convert selected data list to dataframe
schema_Difference = StructType([
    StructField('wayID', StringType(), True),
    StructField('rbt_id', IntegerType(), True),
    StructField('tourCount', IntegerType(), True),
    StructField('timeDifference', FloatType(), True),
])


## using function.py send the packets that include all datas you want to analysis as input
## and return back all ways with packets datas
selected_list = Functions.GetSelected(packets)

if (len(selected_list) != 0):
    # Convert list to RDD
    selected_rdd = sparkSession.sparkContext.parallelize(selected_list)

    # Create data frame
    df_Selected = sparkSession.createDataFrame(selected_rdd, schema_Selected)

    # find a tourCount each way
    turSayısı=df_Selected.filter(df_Selected['wayID']=="-106381").groupBy("wayID","tourCount","datetime").count().orderBy("wayID","tourCount","datetime").collect()

    # convert dataframe df to tempView to enable ask SQL queries.
    df_Selected.createOrReplaceTempView("sqlDF")

    ### travelling time process

    # find a start and finish time interval for each tour and each way
    # and calculate travelling time for each way
    ttDF = sparkSession.sql("select wayID,rbt_id,tourCount,min(datetime),max(datetime) from sqlDF group by wayID,rbt_id,tourCount ").collect()
    ttDF2 = sparkSession.sparkContext.parallelize(ttDF)
    ttDF3 = ttDF2.map(lambda x: (x[0], x[1], x[2], (datetime.datetime.strptime(x[4], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(x[3],'%Y-%m-%d %H:%M:%S.%f')).total_seconds())).collect()

    # Create data frame
    df_TravelTime = sparkSession.createDataFrame(ttDF3, schema_Difference)
    df_TravelTime.createOrReplaceTempView("dfTravelTime")
    travelTimeResult = sparkSession.sql("select wayID,min(timeDifference),max(timeDifference),avg(timeDifference) from dfTravelTime group by wayID").collect()

    ### waiting time process

    # count of different queries
    # print(df_Selected.filter(df_Selected['lineerX'] < 0.0001).count())    # 3561
    # print(df_Selected.filter(df_Selected['lineerX'] < 0.00001).count())   # 1721
    # print(df_Selected.filter(df_Selected['lineerX'] < 0.000001).count())  # 1598
    # print(df_Selected.filter(df_Selected['lineerX'] ==0).count())         # 0
    # print(df_Selected.filter(df_Selected['lineerX'] < 0.001).count())     # 3988
    # print(df_Selected.filter(df_Selected['lineerX'] < 0.01).count())      # 4051
    # print(df_Selected.filter(df_Selected['lineerX'] < 0.05).count())      # 4095


    # find a start and finish time interval for each tour and each way where action=1 that mean is robot was stopped.
    # and calculate waiting time for each way
    wtDF = sparkSession.sql("select wayID,rbt_id,tourCount,min(datetime),max(datetime) from sqlDF where action=1 group by wayID,rbt_id,tourCount ").collect()
    wtDF2 = sparkSession.sparkContext.parallelize(wtDF)
    wtDF3 = wtDF2.map(lambda x: (x[0], x[1], x[2], (datetime.datetime.strptime(x[4], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(x[3],'%Y-%m-%d %H:%M:%S.%f')).total_seconds())).collect()
    # Create data frame
    df_WaitingTime = sparkSession.createDataFrame(wtDF3, schema_Difference)
    df_WaitingTime.createOrReplaceTempView("dfWaitingTime")
    waitingTimeResult = sparkSession.sql("select wayID,min(timeDifference),max(timeDifference),avg(timeDifference) from dfWaitingTime group by wayID").collect()

    ###  average speed process

    # avg_speed = all speed / number of packet
    # for rbt_id
    # df_Selected.groupBy("rbt_id").agg({"lineerX":"mean"})
    # for wayID,rbt_id
    # df_Selected.groupBy("rbt_id").agg({"lineerX":"mean"})
    # for wayID,rbt_id,tourCount
    # ms_WRT=df_Selected.groupBy("wayID","rbt_id","tourCount").agg({"lineerX":"mean"}).collect()

    # find average speed for each way
    averageSpeedResult = sparkSession.sql("select wayID,min(lineerX),max(lineerX),avg(lineerX) from sqlDF group by wayID ").collect()


    ###  density process
    # density = number of robot / way lenght;
    density_rdd = df_Selected.select("wayID", "rbt_id", "wayLength").distinct().groupBy("wayID","wayLength").count().collect()
    density_rdd2 = sparkSession.sparkContext.parallelize(density_rdd)
    densityResult = density_rdd2.map(lambda x: (x[0], x[2] / x[1])).collect()

    ### occupancy process
    #  occupancy = (way length / (all robot lenght))
    occupancy_rdd = df_Selected.select("wayID", "rbt_id", "wayLength", "rbtLength").distinct().groupBy("wayID","wayLength","rbtLength").count().collect()
    occupancy_rdd2 = sparkSession.sparkContext.parallelize(occupancy_rdd)
    occupancy_rdd3 = occupancy_rdd2.map(lambda x: (x[0], x[1] / (x[2] * x[3])))
    occupanyResult = occupancy_rdd3.reduceByKey(lambda x, y: x + y).collect()

    ### prepare data to write MsSQL
    analysisResults = {}

    # add travel time result to analysis dict
    for tt in travelTimeResult:
        analysisSub = []
        analysisSub.append(tt[1])
        analysisSub.append(tt[2])
        analysisSub.append(tt[3])
        analysisResults[tt[0]] = analysisSub

    # add average speed result to analysis dict
    for avgs in averageSpeedResult:
        analysisResults[avgs[0]].append(avgs[1])
        analysisResults[avgs[0]].append(avgs[2])
        analysisResults[avgs[0]].append(avgs[3])

    # add occupancy result to analysis dict
    for occ in occupanyResult:
        analysisResults[occ[0]].append(occ[1])
    # add density result to analysis dict
    for dens in densityResult:
        analysisResults[dens[0]].append(dens[1])

    # create MsSQL connection
    MsSQLConnector1 = MsSQL.MsSQLConnection()
    conn1 = MsSQLConnector1.GetConnection()
    cursor1 = conn1.cursor()

    # get way info from MsSQL
    cursor1.execute("SELECT Way_ID FROM DefWays")

    # find ways that does not have a packet that generated on.
    notExistWay = []
    for way in cursor1:
        check = 0
        for val in travelTimeResult:
            if (str(way[0]) == val[0]):
                check = 1
                break
        if (check == 0):
            notExistWay.append(str(way[0]))

    # get way info from MsSQL
    cursor1.execute("SELECT Way_ID FROM DefWays")
    print("")

    # add waiting time result to analysis dict
    for way in cursor1:
        if (str(way[0]) in notExistWay):
            analysisResults[str(way[0])] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            continue
        else:
            ch = 0
            for val in waitingTimeResult:
                if (str(way[0]) == val[0]):
                    analysisResults[val[0]].append(val[1])
                    analysisResults[val[0]].append(val[2])
                    analysisResults[val[0]].append(val[3])
                    ch = 1
                    break
            if (ch == 0):
                analysisResults[str(way[0])].append(0)
                analysisResults[str(way[0])].append(0)
                analysisResults[str(way[0])].append(0)

    # for the label analysis result, we seperate a hour four part that each has 15 minute and assign them a significant number
    tag = -1
    if (timeMin.minute < 15):
        tag = 1
    elif (timeMin.minute >= 15 and timeMin.minute < 30):
        tag = 2
    elif (timeMin.minute >= 30 and timeMin.minute < 45):
        tag = 3
    else:
        tag = 4

    # generate label like YY/MM/DD/HH/Tag ex: 12/02/2020/14/3  >> date:12/02/2020  hour:14 interval:30-45 minutes
    timeLabel = str(timeMin.year) + "/" + str(timeMin.month) + "/" + str(timeMin.day) + "/" + str(timeMin.hour) + "/" + str(tag)
    #timeLabel="100_tur"

    ### get way information from MsSQL and store analysis result for each way
    cursor1.execute("SELECT Way_ID FROM DefWays")
    ways=[]
    for i in cursor1:
        ways.append(i[0])

    query=""
    try:
        count=0
        for way in ways:
            count+=1
            if(count==len(ways)):
                query+="('"+timeLabel + "'," + str(way) + "," +str(analysisResults[str(way)][3]) + "," + str(analysisResults[str(way)][4]) + "," + str(analysisResults[str(way)][5]) + "," +str(analysisResults[str(way)][0]) + "," + str(analysisResults[str(way)][1]) + "," + str(analysisResults[str(way)][2]) + "," +str(analysisResults[str(way)][8]) + "," + str(analysisResults[str(way)][9]) + "," + str(analysisResults[str(way)][10]) + "," +str(analysisResults[str(way)][6]) + "," + str(analysisResults[str(way)][7]) +")"
            else:
                query+="('"+timeLabel + "'," + str(way) + "," +str(analysisResults[str(way)][3]) + "," + str(analysisResults[str(way)][4]) + "," + str(analysisResults[str(way)][5]) + "," +str(analysisResults[str(way)][0]) + "," + str(analysisResults[str(way)][1]) + "," + str(analysisResults[str(way)][2]) + "," +str(analysisResults[str(way)][8]) + "," + str(analysisResults[str(way)][9]) + "," + str(analysisResults[str(way)][10]) + "," +str(analysisResults[str(way)][6]) + "," + str(analysisResults[str(way)][7]) +"),"

        cursor1.execute("insert into DefAnalysisResult (Anl_timeLabel,Anl_wayID,Anl_speed_min,Anl_speed_max,Anl_speed_avg,Anl_travelTime_min,Anl_travelTime_max,Anl_travelTime_avg,Anl_waitingTime_min,Anl_waitingTime_max,Anl_waitingTime_avg,Anl_occupancy,Anl_density) values "+query)
        conn1.commit()
    except Exception as e :
        print(e)

    ## show all processs time
    print(temptime, "  :  ", datetime.datetime.now(), "  :  ", (datetime.datetime.now() - temptime).total_seconds())
    print("finish")
