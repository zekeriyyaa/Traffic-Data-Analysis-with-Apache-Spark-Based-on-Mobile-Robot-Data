# Traffic-Data-Analysis-with-Spark
A smart factory has many smart systems like autonomous transport vehicle. These all are generate many data like position and speed continuously. So, it is needed to analysis these data and get some useful result. For this purpose, the datas that generated from ATV analyzied with using [Apache Spark](https://spark.apache.org). And desktop app improved and results is visualised for understanding easily using [PyQT5](https://pypi.org/project/PyQt5/).This project has been developed within [CISAR](https://cisar.ogu.edu.tr).

System architecture is shown below:
> <img src="https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/systemArchitecture.PNG" width="590px" height="282px"/>
  
#### [Data-Analysis-with-Spark](https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/tree/master/Data-Analysis-with-Spark)

AGV is generated its current position and speed data 150 times per minute. And these data store MongoDB database as a **document**. Each document has position, speed, datetime and ID datas as shown below. In addition, some information about the way which is ATV is travel on is received from MsSQL database. <br/>

MongoDB document instance:
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/mongodb.png width="240px" height="200px"/>

**Using these datas, five analysis that is shown below is made:**
- **Travel time**: The elapsed time between the ATV starting to task and finishing.
- **Waiting time**: The elapsed time while ATV is waiting during performing its task.
- **Average speed**: The average speed of the ATV while performing its task.
- **Occupancy**: (way lenght) / (number of vehicle * vehicle length)
- **Density**: ( number of vehicle / way length )

#### Installation Steps
Given tools, setups and IDEs used for this project. Given steps is available for Windows installation.
- [python3.7](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) : is a IDE for python (recommended)
- [Apache Spark](https://spark.apache.org/downloads.html) : is a unified analytics engine for large-scale data processing ( **specify version:2.4.5**)
- [Java](https://www.java.com/tr/download/windows-64bit.jsp)
- [pip installer](https://bootstrap.pypa.io/get-pip.py) : download and setup it
- [pyspark](https://pypi.org/project/pyspark/) : is a Python library. specify given version:
```sh
$ pip install pyspark==2.4.5
```
- [winutils](https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe) : download and store it in C:\winutils\bin\ 
- Make winutils executable with given code :
```sh
winutils.exe chmod -R 777 C:\tmp\hive
```
- Change env. variable shown as url
  >	https://www.youtube.com/watch?v=l6L5oyKzHrI&feature=youtu.be <br/> https://medium.com/@sinemhasircioglu/apache-spark-kurulumu-windows-4d411a5c9b43
- Install findspark
```sh
pip install findspark
```
- [pyodbc](https://pypi.org/project/pyodbc/) : is an open source Python module that makes accessing ODBC databases simple.
```sh
pip install pyodbc
```
- [Download ODBC Driver for SQL Server for Windows](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15) : is a single dynamic-link library (DLL) containing run-time support for applications using native-code APIs to connect to SQL Server <br/> Use this selection: **+ msiexec /quiet /passive /qn /i msodbcsql.msi IACCEPTMSODBCSQLLICENSETERMS=YES ADDLOCAL=ALL** <br/>
  [Download ODBC Driver for SQL Server for Linux](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15) <br/> 
