# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 825)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 371, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.cboxTimeLabel = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cboxTimeLabel.setFont(font)
        self.cboxTimeLabel.setCurrentText("")
        self.cboxTimeLabel.setObjectName("cboxTimeLabel")
        self.gridLayout.addWidget(self.cboxTimeLabel, 1, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.cboxYolID = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cboxYolID.setFont(font)
        self.cboxYolID.setObjectName("cboxYolID")
        self.gridLayout.addWidget(self.cboxYolID, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 30, 651, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 631, 271))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_5)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblAvgWt = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblAvgWt.setFont(font)
        self.lblAvgWt.setText("")
        self.lblAvgWt.setObjectName("lblAvgWt")
        self.gridLayout_6.addWidget(self.lblAvgWt, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.lblMinWt = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblMinWt.setFont(font)
        self.lblMinWt.setText("")
        self.lblMinWt.setObjectName("lblMinWt")
        self.gridLayout_6.addWidget(self.lblMinWt, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 2, 0, 1, 1)
        self.lblMaxWt = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblMaxWt.setFont(font)
        self.lblMaxWt.setText("")
        self.lblMaxWt.setObjectName("lblMaxWt")
        self.gridLayout_6.addWidget(self.lblMaxWt, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 291, 91))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblAvgTt = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblAvgTt.setFont(font)
        self.lblAvgTt.setText("")
        self.lblAvgTt.setObjectName("lblAvgTt")
        self.gridLayout_5.addWidget(self.lblAvgTt, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.lblMinTt = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblMinTt.setFont(font)
        self.lblMinTt.setText("")
        self.lblMinTt.setObjectName("lblMinTt")
        self.gridLayout_5.addWidget(self.lblMinTt, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)
        self.lblMaxTt = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblMaxTt.setFont(font)
        self.lblMaxTt.setText("")
        self.lblMaxTt.setObjectName("lblMaxTt")
        self.gridLayout_5.addWidget(self.lblMaxTt, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblAvgSpeed = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblAvgSpeed.setFont(font)
        self.lblAvgSpeed.setText("")
        self.lblAvgSpeed.setObjectName("lblAvgSpeed")
        self.gridLayout_2.addWidget(self.lblAvgSpeed, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lblMinSpeed = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblMinSpeed.setFont(font)
        self.lblMinSpeed.setText("")
        self.lblMinSpeed.setObjectName("lblMinSpeed")
        self.gridLayout_2.addWidget(self.lblMinSpeed, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.lblMaxSpeed = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblMaxSpeed.setFont(font)
        self.lblMaxSpeed.setText("")
        self.lblMaxSpeed.setObjectName("lblMaxSpeed")
        self.gridLayout_2.addWidget(self.lblMaxSpeed, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.lblDensity = QtWidgets.QLabel(self.groupBox_6)
        self.lblDensity.setGeometry(QtCore.QRect(120, 72, 128, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblDensity.setFont(font)
        self.lblDensity.setText("")
        self.lblDensity.setObjectName("lblDensity")
        self.lblOccupancy = QtWidgets.QLabel(self.groupBox_6)
        self.lblOccupancy.setGeometry(QtCore.QRect(120, 44, 128, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblOccupancy.setFont(font)
        self.lblOccupancy.setText("")
        self.lblOccupancy.setObjectName("lblOccupancy")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 72, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(10, 44, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.groupBox_6, 1, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(40, 210, 371, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cboxAnalysisType = QtWidgets.QComboBox(self.groupBox_7)
        self.cboxAnalysisType.setGeometry(QtCore.QRect(120, 40, 241, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cboxAnalysisType.setFont(font)
        self.cboxAnalysisType.setEditable(False)
        self.cboxAnalysisType.setObjectName("cboxAnalysisType")
        self.cboxAnalysisType.addItem("")
        self.cboxAnalysisType.addItem("")
        self.cboxAnalysisType.addItem("")
        self.cboxAnalysisType.addItem("")
        self.cboxAnalysisType.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_2.setGeometry(QtCore.QRect(12, 90, 347, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.setAnalysisResult)
        self.pushButton_2.clicked.connect(MainWindow.setGraphic)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analiz Görselleştirme Programı"))
        self.groupBox.setTitle(_translate("MainWindow", "Analiz Özellik Seçimi"))
        self.label_1.setText(_translate("MainWindow", "Yol ID:"))
        self.label_2.setText(_translate("MainWindow", "Zaman Aralığı:"))
        self.pushButton.setText(_translate("MainWindow", "Değerleri Göster"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Analiz Sonuçları"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Bekleme Süresi"))
        self.label_17.setText(_translate("MainWindow", "Minimum:"))
        self.label_18.setText(_translate("MainWindow", "Ortalama:"))
        self.label_19.setText(_translate("MainWindow", "Maksimum:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Seyahat Süresi"))
        self.label_14.setText(_translate("MainWindow", "Minimum:"))
        self.label_15.setText(_translate("MainWindow", "Ortalama:"))
        self.label_16.setText(_translate("MainWindow", "Maksimum:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Hız"))
        self.label_4.setText(_translate("MainWindow", "Minimum:"))
        self.label_9.setText(_translate("MainWindow", "Ortalama:"))
        self.label_10.setText(_translate("MainWindow", "Maksimum:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Diğer"))
        self.label_5.setText(_translate("MainWindow", "Yoğunluk:"))
        self.label_20.setText(_translate("MainWindow", "Doluluk:"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Analiz Grafikte Gösterim"))
        self.label_3.setText(_translate("MainWindow", "Analiz Türü:"))
        self.cboxAnalysisType.setCurrentText(_translate("MainWindow", "Hız"))
        self.cboxAnalysisType.setItemText(0, _translate("MainWindow", "Hız"))
        self.cboxAnalysisType.setItemText(1, _translate("MainWindow", "Seyahat Süresi"))
        self.cboxAnalysisType.setItemText(2, _translate("MainWindow", "Bekleme Süresi"))
        self.cboxAnalysisType.setItemText(3, _translate("MainWindow", "Yoğunluk"))
        self.cboxAnalysisType.setItemText(4, _translate("MainWindow", "Doluluk"))
        self.pushButton_2.setText(_translate("MainWindow", "Grafikte Göster"))

