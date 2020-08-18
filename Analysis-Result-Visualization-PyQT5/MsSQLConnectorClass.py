import pyodbc
class MsSQLConnection:
    __server="SERVERNAME"
    __database = 'DATABASENAME'
    __conn="null"

    def __init__(self,server="SERVERNAME",database= 'DATABASENAME'):
        self.__server=server
        self.__database=database
        self.__conn=self.__GetConnect()

    def __SetConnection(self):
        self.__conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                              'Server='+self.__server+';'
                              'Database='+self.__database+';'
                              'Trusted_Connection=yes;')

    def __GetConnect(self):
        if(self.__conn=="null"):
            self.__SetConnection()
        return self.__conn

    def GetConnection(self):
        return self.__conn
