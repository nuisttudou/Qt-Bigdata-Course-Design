# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tudou/桌面/bigdata/qt_try/fir/de2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(460, 570, 80, 25))
        self.exitButton.setAutoDefault(False)
        self.exitButton.setObjectName("exitButton")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(360, 570, 80, 25))
        self.runButton.setObjectName("runButton")
        self.content_plot = QtWidgets.QWidget(self.centralwidget)
        self.content_plot.setGeometry(QtCore.QRect(40, 20, 500, 500))
        self.content_plot.setObjectName("content_plot")
        self.class_num_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.class_num_lineEdit.setGeometry(QtCore.QRect(10, 570, 113, 25))
        self.class_num_lineEdit.setObjectName("class_num_lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 540, 111, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 22))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setCheckable(False)
        self.open_action.setObjectName("open_action")
        self.k_mean_action = QtWidgets.QAction(MainWindow)
        self.k_mean_action.setObjectName("k_mean_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.actiontemp = QtWidgets.QAction(MainWindow)
        self.actiontemp.setObjectName("actiontemp")
        self.k_medoids_action = QtWidgets.QAction(MainWindow)
        self.k_medoids_action.setObjectName("k_medoids_action")
        self.actionrandom = QtWidgets.QAction(MainWindow)
        self.actionrandom.setObjectName("actionrandom")
        self.actionMiniBatchKMeans = QtWidgets.QAction(MainWindow)
        self.actionMiniBatchKMeans.setObjectName("actionMiniBatchKMeans")
        self.menumenu.addAction(self.open_action)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.k_mean_action)
        self.menumenu.addAction(self.k_medoids_action)
        self.menumenu.addAction(self.actionMiniBatchKMeans)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionrandom)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.exit_action)
        self.menubar.addAction(self.menumenu.menuAction())

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        self.exit_action.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitButton.setText(_translate("MainWindow", "exit"))
        self.runButton.setText(_translate("MainWindow", "run"))
        self.label.setText(_translate("MainWindow", "簇类数"))
        self.menumenu.setTitle(_translate("MainWindow", "菜单"))
        self.open_action.setText(_translate("MainWindow", "导入数据"))
        self.k_mean_action.setText(_translate("MainWindow", "K-means"))
        self.exit_action.setText(_translate("MainWindow", "exit"))
        self.actiontemp.setText(_translate("MainWindow", "temp"))
        self.k_medoids_action.setText(_translate("MainWindow", "K-中心点聚类"))
        self.actionrandom.setText(_translate("MainWindow", "random"))
        self.actionMiniBatchKMeans.setText(_translate("MainWindow", "MiniBatchKMeans"))
