# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 11, 1, 1, 1)
        self.fio2_slider = QtWidgets.QSlider(self.centralwidget)
        self.fio2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fio2_slider.setObjectName("fio2_slider")
        self.gridLayout.addWidget(self.fio2_slider, 13, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 15, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 13, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 7, 1, 1, 1)
        self.plateau_press_label = QtWidgets.QLabel(self.centralwidget)
        self.plateau_press_label.setObjectName("plateau_press_label")
        self.gridLayout.addWidget(self.plateau_press_label, 7, 0, 1, 1)
        self.tv_label = QtWidgets.QLabel(self.centralwidget)
        self.tv_label.setObjectName("tv_label")
        self.gridLayout.addWidget(self.tv_label, 9, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 15, 4, 1, 1)
        self.ie_label = QtWidgets.QLabel(self.centralwidget)
        self.ie_label.setObjectName("ie_label")
        self.gridLayout.addWidget(self.ie_label, 11, 0, 1, 1)
        self.ie_slider = QtWidgets.QSlider(self.centralwidget)
        self.ie_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ie_slider.setObjectName("ie_slider")
        self.gridLayout.addWidget(self.ie_slider, 11, 3, 1, 1)
        self.resp_rate_label = QtWidgets.QLabel(self.centralwidget)
        self.resp_rate_label.setObjectName("resp_rate_label")
        self.gridLayout.addWidget(self.resp_rate_label, 15, 0, 1, 1)
        self.resp_rate_slider = QtWidgets.QSlider(self.centralwidget)
        self.resp_rate_slider.setOrientation(QtCore.Qt.Horizontal)
        self.resp_rate_slider.setObjectName("resp_rate_slider")
        self.gridLayout.addWidget(self.resp_rate_slider, 15, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 6, 2, 1, 1)
        self.resp_rate_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.resp_rate_lcd.setObjectName("resp_rate_lcd")
        self.gridLayout.addWidget(self.resp_rate_lcd, 15, 2, 1, 1)
        self.tv_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.tv_lcd.setObjectName("tv_lcd")
        self.gridLayout.addWidget(self.tv_lcd, 9, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 12, 2, 1, 1)
        self.ie_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.ie_lcd.setObjectName("ie_lcd")
        self.gridLayout.addWidget(self.ie_lcd, 11, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 10, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 4, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 5, 1, 1, 1)
        self.plateau_press_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.plateau_press_lcd.setObjectName("plateau_press_lcd")
        self.gridLayout.addWidget(self.plateau_press_lcd, 7, 2, 1, 1)
        self.fio2_label = QtWidgets.QLabel(self.centralwidget)
        self.fio2_label.setObjectName("fio2_label")
        self.gridLayout.addWidget(self.fio2_label, 13, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 2, 2, 1, 1)
        self.peep_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.peep_lcd.setObjectName("peep_lcd")
        self.gridLayout.addWidget(self.peep_lcd, 3, 2, 1, 1)
        self.fio2_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.fio2_lcd.setObjectName("fio2_lcd")
        self.gridLayout.addWidget(self.fio2_lcd, 13, 2, 1, 1)
        self.mode_button = QtWidgets.QPushButton(self.centralwidget)
        self.mode_button.setCheckable(True)
        self.mode_button.setObjectName("mode_button")
        self.gridLayout.addWidget(self.mode_button, 1, 2, 1, 1)
        self.mode_label = QtWidgets.QLabel(self.centralwidget)
        self.mode_label.setObjectName("mode_label")
        self.gridLayout.addWidget(self.mode_label, 1, 0, 1, 1)
        self.peak_press_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.peak_press_lcd.setObjectName("peak_press_lcd")
        self.gridLayout.addWidget(self.peak_press_lcd, 5, 2, 1, 1)
        self.peak_press_label = QtWidgets.QLabel(self.centralwidget)
        self.peak_press_label.setObjectName("peak_press_label")
        self.gridLayout.addWidget(self.peak_press_label, 5, 0, 1, 1)
        self.peep_label = QtWidgets.QLabel(self.centralwidget)
        self.peep_label.setObjectName("peep_label")
        self.gridLayout.addWidget(self.peep_label, 3, 0, 1, 1)
        self.tv_slider = QtWidgets.QSlider(self.centralwidget)
        self.tv_slider.setOrientation(QtCore.Qt.Horizontal)
        self.tv_slider.setObjectName("tv_slider")
        self.gridLayout.addWidget(self.tv_slider, 9, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 14, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 16, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plateau_press_label.setText(_translate("MainWindow", "Plateau Pressure"))
        self.tv_label.setText(_translate("MainWindow", "Tidal Volume"))
        self.ie_label.setText(_translate("MainWindow", "I/E Ratio"))
        self.resp_rate_label.setText(_translate("MainWindow", "Resp. Rate"))
        self.fio2_label.setText(_translate("MainWindow", "FiO2"))
        self.mode_button.setText(_translate("MainWindow", "SIMV"))
        self.mode_label.setText(_translate("MainWindow", "Mode"))
        self.peak_press_label.setText(_translate("MainWindow", "Peak. Inspiratory Pressure"))
        self.peep_label.setText(_translate("MainWindow", "PEEP"))
