from PyQt5.QtWidgets import*
from userInterface import Ui_MainWindow
import MsSQLConnectorClass as MsSQL
import datetime
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg



class visualisation(QMainWindow):
    # create MsSQL class object and set connection with default value that placed in class
    MsSQLConnector = MsSQL.MsSQLConnection()
    conn = MsSQLConnector.GetConnection()
    cursor = conn.cursor()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cboxYolID.addItems(self.getWayIDFromDB())
        self.ui.cboxTimeLabel.addItems(self.getTimeLabelFromDB())

        #self.conn.close()

    def getWayIDFromDB(self):
        ### get wayIDs from MsSQL
        self.cursor.execute("SELECT Anl_wayID FROM DefAnalysisResult group by Anl_wayID")
        wayIDs=[]
        for i in self.cursor:
            wayIDs.append(str(i[0]))
        return wayIDs

    def getTimeLabelFromDB(self):
        ### get analysis result from MsSQL
        self.cursor.execute("SELECT Anl_timeLabel FROM DefAnalysisResult group by Anl_timeLabel order by Anl_timeLabel")
        times=[]
        for i in self.cursor:
            times.append(str(i[0]))
        return times

    def setAnalysisResult(self):
        # set analysis result info into interface
        wayID = self.ui.cboxYolID.currentText()
        timeLabel = self.ui.cboxTimeLabel.currentText()
        # get selected way' info from MsSQL
        self.cursor.execute("SELECT * FROM DefAnalysisResult where Anl_wayID=" + wayID + " and Anl_timeLabel='" + timeLabel + "'")
        results = self.cursor.fetchone()
        self.ui.lblMinSpeed.setText(str(round(results[3],7)))
        self.ui.lblMaxSpeed.setText(str(round(results[4],7)))
        self.ui.lblAvgSpeed.setText(str(round(results[5],7)))
        self.ui.lblMinTt.setText(str(round(results[6],7)))
        self.ui.lblMaxTt.setText(str(round(results[7],7)))
        self.ui.lblAvgTt.setText(str(round(results[8],7)))
        self.ui.lblMinWt.setText(str(round(results[9],7)))
        self.ui.lblMaxWt.setText(str(round(results[10],7)))
        self.ui.lblAvgWt.setText(str(round(results[11],7)))
        self.ui.lblOccupancy.setText(str(round(results[12],7)))
        self.ui.lblDensity.setText(str(round(results[13],7)))

    def setGraphic(self):
        ### get way' coordinate from MsSQL to set on graphic
        self.cursor.execute("SELECT w.Way_ID,nd.Nd_Latitute,nd.Nd_Longtitute,wp.Wyp_EnterExitCode FROM ((DefWays as w INNER JOIN DefWaypoints as wp on w.Way_ID=wp.Wyp_WayID ) INNER JOIN DefNodes as nd ON nd.Nd_ID=wp.Wyp_NodeID) where wp.Wyp_EnterExitCode in (0,1) order by w.Way_ID,wp.Wyp_EnterExitCode")
        waysCoordinate = []
        for i in self.cursor:
            waysCoordinate.append(i)

        timeLabel = self.ui.cboxTimeLabel.currentText()
        tag=""
        content=""
        if(self.ui.cboxAnalysisType.currentText()=="Hız"):
            tag="Hız"
            content="Anl_speed_avg"
        elif(self.ui.cboxAnalysisType.currentText()=="Seyahat Süresi"):
            tag="Seyahat Süresi"
            content="Anl_travelTime_avg"
        elif(self.ui.cboxAnalysisType.currentText()=="Bekleme Süresi"):
            tag="Bekleme Süresi"
            content="Anl_waitingTime_avg"
        elif(self.ui.cboxAnalysisType.currentText()=="Doluluk"):
            tag="Doluluk"
            content="Anl_occupancy"
        elif(self.ui.cboxAnalysisType.currentText()=="Yoğunluk"):
            tag="Yoğunluk"
            content="Anl_density"


        ### get selected way' analysis result from MsSQL
        self.cursor.execute("SELECT Anl_wayID,"+content+" FROM DefAnalysisResult where Anl_timeLabel='" + timeLabel + "'")

        values=[]
        valuesSum=[]

        for i in self.cursor:
            values.append(i)
            valuesSum.append(i[1])

        # calculate min-max-avg value for selected way
        temp=(max(valuesSum)-min(valuesSum))/3.33
        minTop=min(valuesSum)+temp
        maxBottom=max(valuesSum)-temp

        fig_size = [12,8]
        plt.figure(figsize=fig_size)

        # draw graph
        x1,x2,x3=0,0,0
        for i in waysCoordinate:
            x, y = [], []
            for k in waysCoordinate:
                if(k[0]==i[0]):
                    x.append(k[1])
                    y.append(k[2])
            for j in values:
                if(j[0]==i[0]):
                    if(j[1]<minTop):
                        if(x1==0):
                            plt.plot(x, y, 'o-', color="red",lineWidth=3,label="Düşük "+tag)
                            x1=1
                        else:
                            plt.plot(x, y, 'o-', color="red", lineWidth=3)
                        break
                    elif(j[1]>maxBottom):
                        if(x2==0):
                            plt.plot(x, y, 'o-', color="yellow",lineWidth=3,label="Orta "+tag)
                            x2=1
                        else:
                            plt.plot(x, y, 'o-', color="yellow", lineWidth=3)
                        break
                    else:
                        if(x3==0):
                            plt.plot(x, y, 'o-', color="green",lineWidth=3,label="Yüksek "+tag)
                            x3=1
                        else:
                            plt.plot(x, y, 'o-', color="green", lineWidth=3)
                        break

        plt.title("Analiz Sonuçları")
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        #plt.legend(["Düşük Hız","Orta Hız","Yüksek Hız"])
        plt.legend()
        plt.show()

        ### get selected timeLabel
        self.cursor.execute("SELECT * FROM DefAnalysisResult where Anl_timeLabel='"+self.ui.cboxTimeLabel.currentText()+"'")
        analysis = []
        for i in self.cursor:
            analysis.append(i)

        print("")


uygulama = QApplication([])
pencere = visualisation()
pencere.show()
uygulama.exec_()