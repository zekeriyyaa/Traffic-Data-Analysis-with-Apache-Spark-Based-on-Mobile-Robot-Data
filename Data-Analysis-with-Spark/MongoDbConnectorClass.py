from pyspark.sql import SparkSession

class MongoDBConnection:

    ##for localhost connection
    __host = "127.0.0.1"
    __database = "dbAkilliFabrikaTest"
    __collection = "Collection6"

    ##for server connection
    __host = "192.168.8.155"
    __host = "127.0.0.1"
    __database = "dbAkilliFabrikaAR"
    __collection = "Konum"

    # Structure the connection
    #__connectionString = "mongodb://{0}:{1}@{2}:{3}/{4}.{5}?ssl=true&replicaSet=globaldb".format(userName, primaryKey, __host, port, __database, __collection)
    __connectionString="mongodb://"+__host+"/"+__database+"."+__collection

    __spark="null"

    def __init__(self,host="127.0.0.1",database="dbAkilliFabrikaAR",collection="Konum"):
        self.__host=host
        self.__database=database
        self.__collection=collection
        self.__spark=self.__GetSparkSessionPrivate()

    def __SetSparkSession(self):
        self.__spark = SparkSession \
            .builder \
            .config('spark.mongodb.input.uri', self.__connectionString) \
            .config('spark.mongodb.output.uri', self.__connectionString) \
            .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.4.1') \
            .getOrCreate()

    def __GetSparkSessionPrivate(self):
        if(self.__spark=="null"):
            self.__SetSparkSession()
        return self.__spark

    def GetSparkSession(self):
        return self.__spark

    def GetConnectionString(self):
        return self.__connectionString

    def GetDatabase(self):
        return self.__database

    def GetCollection(self):
        return self.__collection
