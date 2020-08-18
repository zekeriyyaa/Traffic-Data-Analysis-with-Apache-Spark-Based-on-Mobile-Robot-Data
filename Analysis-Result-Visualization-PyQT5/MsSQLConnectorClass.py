import pyodbc
class MsSQLConnection:
    __server="DESKTOP-6PMNDOG"
    __database = 'dbAkilliFabrika'
    __conn="null"

    def __init__(self,server="DESKTOP-6PMNDOG",database= 'dbAkilliFabrika'):
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