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
        MainWindow.resize(705, 854)
        MainWindow.setMinimumSize(QtCore.QSize(650, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(650, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setEnabled(True)
        self.tab1.setObjectName("tab1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 652, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kmeans_content_plot = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.kmeans_content_plot.setMinimumSize(QtCore.QSize(650, 0))
        self.kmeans_content_plot.setMaximumSize(QtCore.QSize(650, 16777215))
        self.kmeans_content_plot.setObjectName("kmeans_content_plot")
        self.verticalLayout_2.addWidget(self.kmeans_content_plot)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(10000, 100))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(230, 0))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.radioButton_kmeans_plusplus = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_kmeans_plusplus.setObjectName("radioButton_kmeans_plusplus")
        self.horizontalLayout_2.addWidget(self.radioButton_kmeans_plusplus)
        self.radioButton_kmeans_random = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_kmeans_random.setChecked(True)
        self.radioButton_kmeans_random.setObjectName("radioButton_kmeans_random")
        self.horizontalLayout_2.addWidget(self.radioButton_kmeans_random)
        self.radioButton_kmeans_heuristic = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_kmeans_heuristic.setObjectName("radioButton_kmeans_heuristic")
        self.horizontalLayout_2.addWidget(self.radioButton_kmeans_heuristic)
        self.gridLayout_2.addWidget(self.widget_2, 2, 3, 1, 1)
        self.runButton_kMeans = QtWidgets.QPushButton(self.widget)
        self.runButton_kMeans.setObjectName("runButton_kMeans")
        self.gridLayout_2.addWidget(self.runButton_kMeans, 1, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 55, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_kmeans_runtimes = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_kmeans_runtimes.setGeometry(QtCore.QRect(100, 0, 113, 25))
        self.lineEdit_kmeans_runtimes.setObjectName("lineEdit_kmeans_runtimes")
        self.gridLayout_2.addWidget(self.widget_5, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 652, 621))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.kmedoids_content_plot = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.kmedoids_content_plot.setMinimumSize(QtCore.QSize(650, 0))
        self.kmedoids_content_plot.setMaximumSize(QtCore.QSize(650, 16777215))
        self.kmedoids_content_plot.setObjectName("kmedoids_content_plot")
        self.verticalLayout_4.addWidget(self.kmedoids_content_plot)
        self.widget_3 = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setMinimumSize(QtCore.QSize(230, 0))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.radioButton_kmedoids_heuristic = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_kmedoids_heuristic.setObjectName("radioButton_kmedoids_heuristic")
        self.horizontalLayout.addWidget(self.radioButton_kmedoids_heuristic)
        self.radioButton_kmedoids_random = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_kmedoids_random.setChecked(True)
        self.radioButton_kmedoids_random.setObjectName("radioButton_kmedoids_random")
        self.horizontalLayout.addWidget(self.radioButton_kmedoids_random)
        self.radioButton_kmedoids_plusplus = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_kmedoids_plusplus.setObjectName("radioButton_kmedoids_plusplus")
        self.horizontalLayout.addWidget(self.radioButton_kmedoids_plusplus)
        self.gridLayout_4.addWidget(self.widget_4, 1, 1, 1, 1)
        self.runButton_KMedoids = QtWidgets.QPushButton(self.widget_3)
        self.runButton_KMedoids.setObjectName("runButton_KMedoids")
        self.gridLayout_4.addWidget(self.runButton_KMedoids, 0, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.comboBox_kMedoids = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_kMedoids.setGeometry(QtCore.QRect(110, 10, 111, 25))
        self.comboBox_kMedoids.setObjectName("comboBox_kMedoids")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.comboBox_kMedoids.addItem("")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.widget_6, 1, 4, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.setObjectName("randomButton")
        self.gridLayout_3.addWidget(self.randomButton, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setAutoDefault(False)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_3.addWidget(self.exitButton, 2, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.class_num_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.class_num_lineEdit.setObjectName("class_num_lineEdit")
        self.gridLayout_3.addWidget(self.class_num_lineEdit, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_max_iter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_max_iter.setObjectName("lineEdit_max_iter")
        self.gridLayout_3.addWidget(self.lineEdit_max_iter, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox_Voronoi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Voronoi.setObjectName("checkBox_Voronoi")
        self.gridLayout_3.addWidget(self.checkBox_Voronoi, 1, 4, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_3.addWidget(self.horizontalSlider, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.label_evaluat = QtWidgets.QLabel(self.centralwidget)
        self.label_evaluat.setText("")
        self.label_evaluat.setObjectName("label_evaluat")
        self.verticalLayout_3.addWidget(self.label_evaluat)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 22))
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
        self.tabWidget.setCurrentIndex(1)
        self.exitButton.clicked.connect(MainWindow.close)
        self.exit_action.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "初始化方法"))
        self.radioButton_kmeans_plusplus.setText(_translate("MainWindow", "heuristic"))
        self.radioButton_kmeans_random.setText(_translate("MainWindow", "random"))
        self.radioButton_kmeans_heuristic.setText(_translate("MainWindow", "k-means++"))
        self.runButton_kMeans.setText(_translate("MainWindow", "run"))
        self.label_5.setText(_translate("MainWindow", "运行次数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "kMeans"))
        self.label_4.setText(_translate("MainWindow", "初始化方法"))
        self.radioButton_kmedoids_heuristic.setText(_translate("MainWindow", "heuristic"))
        self.radioButton_kmedoids_random.setText(_translate("MainWindow", "random"))
        self.radioButton_kmedoids_plusplus.setText(_translate("MainWindow", "k-medoids++"))
        self.runButton_KMedoids.setText(_translate("MainWindow", "run"))
        self.comboBox_kMedoids.setItemText(0, _translate("MainWindow", "euclidean"))
        self.comboBox_kMedoids.setItemText(1, _translate("MainWindow", "l2"))
        self.comboBox_kMedoids.setItemText(2, _translate("MainWindow", "l1"))
        self.comboBox_kMedoids.setItemText(3, _translate("MainWindow", "manhattan"))
        self.comboBox_kMedoids.setItemText(4, _translate("MainWindow", "cityblock"))
        self.comboBox_kMedoids.setItemText(5, _translate("MainWindow", "braycurtis"))
        self.comboBox_kMedoids.setItemText(6, _translate("MainWindow", "canberra"))
        self.comboBox_kMedoids.setItemText(7, _translate("MainWindow", "chebyshev"))
        self.comboBox_kMedoids.setItemText(8, _translate("MainWindow", "correlation"))
        self.comboBox_kMedoids.setItemText(9, _translate("MainWindow", "cosine"))
        self.comboBox_kMedoids.setItemText(10, _translate("MainWindow", "dice"))
        self.comboBox_kMedoids.setItemText(11, _translate("MainWindow", "hamming"))
        self.comboBox_kMedoids.setItemText(12, _translate("MainWindow", "jaccard"))
        self.comboBox_kMedoids.setItemText(13, _translate("MainWindow", "kulsinski"))
        self.comboBox_kMedoids.setItemText(14, _translate("MainWindow", "mahalanobis"))
        self.comboBox_kMedoids.setItemText(15, _translate("MainWindow", "matching"))
        self.comboBox_kMedoids.setItemText(16, _translate("MainWindow", "minkowski"))
        self.comboBox_kMedoids.setItemText(17, _translate("MainWindow", "rogerstanimoto"))
        self.comboBox_kMedoids.setItemText(18, _translate("MainWindow", "russellrao"))
        self.comboBox_kMedoids.setItemText(19, _translate("MainWindow", "seuclidean"))
        self.comboBox_kMedoids.setItemText(20, _translate("MainWindow", "sokalmichener"))
        self.comboBox_kMedoids.setItemText(21, _translate("MainWindow", "sokalsneath"))
        self.comboBox_kMedoids.setItemText(22, _translate("MainWindow", "sqeuclidean"))
        self.comboBox_kMedoids.setItemText(23, _translate("MainWindow", "yule"))
        self.comboBox_kMedoids.setItemText(24, _translate("MainWindow", "wminkowski"))
        self.comboBox_kMedoids.setItemText(25, _translate("MainWindow", "haversine"))
        self.label_6.setText(_translate("MainWindow", "距离度量方法"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "kMedoids"))
        self.randomButton.setText(_translate("MainWindow", "random"))
        self.label.setText(_translate("MainWindow", "簇类数"))
        self.exitButton.setText(_translate("MainWindow", "exit"))
        self.label_3.setText(_translate("MainWindow", "最大迭代次数"))
        self.checkBox_Voronoi.setText(_translate("MainWindow", "沃罗诺伊图"))
        self.label_7.setText(_translate("MainWindow", "密集                  随机点                  稀疏"))
        self.menumenu.setTitle(_translate("MainWindow", "菜单"))
        self.open_action.setText(_translate("MainWindow", "导入数据"))
        self.k_mean_action.setText(_translate("MainWindow", "K-means"))
        self.exit_action.setText(_translate("MainWindow", "exit"))
        self.actiontemp.setText(_translate("MainWindow", "temp"))
        self.k_medoids_action.setText(_translate("MainWindow", "K-中心点聚类"))
        self.actionrandom.setText(_translate("MainWindow", "random"))
        self.actionMiniBatchKMeans.setText(_translate("MainWindow", "MiniBatchKMeans"))
