#### [Analysis-Result-Visualization-PyQT5](https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/tree/master/Analysis-Result-Visualization-PyQT5)
The desktop app is improved. So, result of the analysis has visualized to easly understanding. At the app, you can select way and time interval which to show all analysis result. 
The desktop app look like as shown below:
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/appInterface.png width="750px" height="270px"/>

And also you can select which type of analysis that you want to visualized for a way that you already specified.
The speed analysis of all way is shown as below ( **red**: low speed **green**: medium speed **yellow**: high speed ) :
> <img src=https://github.com/zekeriyyaa/Traffic-Data-Analysis-with-Spark/blob/master/images/speedGraph.png width="600px" height="300px"/>

#### Installation Steps
Given tools, setups and IDEs used for this project. Given steps is available for Windows installation.
- [python3.5](https://www.python.org/downloads/) : specify version 3.5
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) : is a IDE for python (recommended)
- [QtDesigner](https://build-system.fman.io/qt-designer-download) : a interface designer
- [pyodbc](https://pypi.org/project/pyodbc/) : is an open source Python module that makes accessing ODBC databases simple.
```sh
pip install pyodbc
```
- [pyqtgraph](https://pypi.org/project/pyqtgraph/) : is a pure-python graphics and GUI library built on PyQt4/PyQt5/PySide/PySide2 and numpy.
```sh
pip install pyqtgraph
```

#### Usage
After the design is completed, QtDesigner produce file has .ui extension. So, you need to convert this file to python file and you can import design file by another python file. **pyuic.bat** is convert .ui ext file to .py file with help given code : 
```sh
C:\Users\zekeriyya\AppData\Local\Programs\Python\Python35\Lib\site-packages\PyQt5\pyuic5.bat inputFileName.ui -o outputFileName.py
```
