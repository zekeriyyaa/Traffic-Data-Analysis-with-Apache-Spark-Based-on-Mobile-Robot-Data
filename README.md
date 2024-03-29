# Traffic-Data-Analysis-with-Spark-Based-on-Autonomous-Transport-Vehicle-Data
There could be a traffic in smart factories caused by autonomous transport vehicles (ATVs). So, it is needed to analyzed the data generated by ATV and produce useful feedback to system to enhance the system productivity. For this purpose, five analysis are done such as travel time, waiting time, average speed, occupancy and density and the results were visualized. 

The data that generated from AGV analyzied with using [Apache Spark](https://spark.apache.org). And desktop app improved and results is visualised for understanding easily using [PyQT5](https://pypi.org/project/PyQt5/).This project has been developed within [ifarlab](https://ifarlab.ogu.edu.tr).

System architecture is shown below:
> <img src="https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/systemArchitecture.PNG" width="590px" height="282px"/>
  
#### [Data-Analysis-with-Spark](https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/tree/master/Data-Analysis-with-Spark)

ATV generates current position and speed data 150 times per minute. And these data store MongoDB database as a **document**. Each document has position, speed, datetime and ID datas as shown below. In addition, some information about the way is obtained from the MSSQL database. <br/>

MongoDB document instance:
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/mongodb.png width="240px" height="200px"/>

**Using these datas, five analysis that is shown below is made:**
- **Travel time**: The elapsed time between the ATV starting to task and finishing.
- **Waiting time**: The elapsed time while ATV is waiting during performing its task.
- **Average speed**: The average speed of the ATV while performing its task.
- **Occupancy**: (way lenght) / (number of vehicle * vehicle length) 
- **Density**: ( number of vehicle / way length )


#### [Analysis-Result-Visualization-PyQT5](https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/tree/master/Analysis-Result-Visualization-PyQT5)
The desktop app is improved. So, result of the analysis has visualized to easly understanding. At the app, you can select way and time interval which to show all analysis result. 
The desktop app look like as shown below:
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/appInterface.png width="750px" height="300px"/>

And also you can select which type of analysis that you want to visualized for a way that you already specified.
The speed analysis of all way is shown as below ( **red**: low speed **green**: medium speed **yellow**: high speed ) :
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/speedGraph.png width="600px" height="300px"/>












