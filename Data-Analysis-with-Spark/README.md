# Traffic-Data-Analysis-with-Spark
A smart factory has many smart systems like autonomous guided vehicle. These all are generate many data like position and speed continuously. So, it is needed to analysis these data and get some useful result. For this purpose, the datas that generated from AGV analyzied with using [Apache Spark](https://spark.apache.org). And desktop app improved and results is visualised for understanding easily using [PyQT5](https://pypi.org/project/PyQt5/).This project has been developed within [CISAR](https://cisar.ogu.edu.tr).

System architecture is shown below:
> <img src="https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/systemArchitecture.PNG" width="590px" height="282px"/>
  
#### [Data-Analysis-with-Spark](https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/tree/master/Data-Analysis-with-Spark)

AGV is generated its current position and speed data 150 times per minute. And these data store MongoDB database as a **packet**. Each packet has position, speed, datetime and ID datas as shown below. In addition, some information about the way which is AGV is travel on is received from MsSQL database. <br/>

MongoDB packet instance:
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/mongodb.png width="240px" height="200px"/>

**Using these datas, five analysis that is shown below is made:**
- **Travel time**: A time between AGV start moving and stop. It is reached for each way and vehicle separately.
- **Waiting time**: A time between AGV stoped and start moving again. It is reached for each way and vehicle separately.
- **Average speed**: AGV's average speed. It is reached for each way separately.
- **Occupancy**: It is reached for each way seperately. (way lenght) / (number of vehicle * vehicle length) 
- **Density**: It is reached for aech way separately.  ( number of vehicle / way length )
