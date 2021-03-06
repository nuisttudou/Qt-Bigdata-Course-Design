from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QAbstractItemView
from matplotlib.backends.backend_qt5agg import FigureCanvas

from sklearn import metrics
from de2 import Ui_MainWindow  # importing our generated file
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs
import pandas as pd
from sklearn_extra.cluster import KMedoids
import random
from Voronoi_Diagram_ import *
from mpl_toolkits.mplot3d import Axes3D

RANDOM_VAL = 3
RANDOM_NUM = 1500

centroids=None

class datein():#数据输入类
    def __init__(self, pwd=""):
        if pwd == "":
            return
        da = np.array(pd.read_csv(pwd))
        self.x_varied, self.y_varied = da[:, 0:da.shape[1] - 1], da[:, da.shape[1] - 1]


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):#主界面
    def evaluate(self, model, y_pred, ):#聚类评估算法
        print('inertia\thomo\tcompl\tv-meas\tARI\tAMI')
        print('%.3f\t%.3f\t%.3f\t%.3f\t%.3f'  # \t%.3f'
              % (
                  metrics.homogeneity_score(y_pred, self.data.y_varied),
                  metrics.completeness_score(y_pred, self.data.y_varied),
                  metrics.v_measure_score(y_pred, self.data.y_varied),
                  metrics.adjusted_rand_score(y_pred, self.data.y_varied),
                  metrics.adjusted_mutual_info_score(y_pred, self.data.y_varied),
                  #  metrics.silhouette_score(y_pred, self.data.y_varied,metric='euclidean')
              ))

        eva_string = "homo:" + str(round(metrics.homogeneity_score(y_pred, self.data.y_varied), 3)) + '\n' + \
                     "compl:" + str(round(metrics.completeness_score(y_pred, self.data.y_varied), 3)) + '\n' + \
                     "v-meas:" + str(round(metrics.v_measure_score(y_pred, self.data.y_varied), 3)) + '\n' + \
                     "ARI:" + str(round(metrics.adjusted_rand_score(y_pred, self.data.y_varied), 3)) + '\n' + \
                     "AMI:" + str(round(metrics.adjusted_mutual_info_score(y_pred, self.data.y_varied), 3))
        self.ui.label_evaluat.setText(eva_string)

        temp = ""
        print(centroids)
        if centroids is not None:
            for class_pred in set(y_pred):
                midl=round(centroids[class_pred][0],2)
                midr=round(centroids[class_pred][1],2)

                mid=str((midl,midr))
                temp += chr(65 + class_pred) + ":" + str(np.sum(y_pred == class_pred))+" "+ mid + "\n"
        else:
            for class_pred in set(y_pred):
                temp += chr(65 + class_pred) + ":" + str(np.sum(y_pred == class_pred)) + "\n"
        self.ui.label_count.setText(temp)

    def add_datax_table(self):#右侧表格
        def table_clear_ALL(self):#清空表格
            for index in range(0, self.ui.tableWidget.rowCount()).__reversed__():
                self.ui.tableWidget.removeRow(index)

        table_clear_ALL(self)

        def add_data_table_one_row(self, l):#表格加一行
            self.ui.tableWidget.setColumnCount(l.shape[0] + 1)
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)

            # item_id = QTableWidgetItem('%.3f' % (l[0]))  # str(l[0]))
            # item_name = QTableWidgetItem('%.3f' % (l[1]))  # str(l[1]))
            # item_pos = QTableWidgetItem('???')
            # self.ui.tableWidget.setItem(row, 0, item_id)
            # self.ui.tableWidget.setItem(row, 1, item_name)
            # self.ui.tableWidget.setItem(row, 2, item_pos)

            for s in range(0, l.shape[0]):
                self.ui.tableWidget.setItem(row, s, QTableWidgetItem('%.3f' % (l[s])))
            self.ui.tableWidget.setItem(row, l.shape[0], QTableWidgetItem('???'))

        for xRow in self.data.x_varied:
            add_data_table_one_row(self, xRow)

    def add_datay_table(self, y_pred):#添加表格中的类别一项
        ind = self.data.x_varied.shape[1]
        for yIndex in range(0, y_pred.shape[0]):
            self.ui.tableWidget.setItem(yIndex, ind, QTableWidgetItem(chr(y_pred[yIndex] + 65)))
        # for yIndex in range(0,y_pred.shape[0]):
        #     self.ui.tableWidget.setItem(yIndex, 2, QTableWidgetItem(str(y_pred[yIndex])))
        # for yIndex in range(0,self.data.y_varied.shape[0]):
        #     self.ui.tableWidget.setItem(yIndex, 2, QTableWidgetItem(str(self.data.y_varied[yIndex])))

    def setRandData(self):#设置随机数据集
        self.data = datein()
        centers_num = int(self.ui.horizontalSlider.value())
        cluster_std_ = [random.random() * RANDOM_VAL for _ in range(centers_num)]
        self.data.x_varied, self.data.y_varied = make_blobs(n_samples=RANDOM_NUM, cluster_std=cluster_std_,
                                                            # cluster_std=2
                                                            centers=centers_num)  # , cluster_std=[1.0, 2.5, 0.5])

        # self.add_data_table('x', 'y', 'z')
        self.add_datax_table()

        print("random OK")

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = None

        self.layy = QtWidgets.QVBoxLayout(self.ui.kmeans_content_plot)
        self.ui.plotWidget = None

        self.layy_KMedoids = QtWidgets.QVBoxLayout(self.ui.kmedoids_content_plot)
        self.ui.plotWidget_KMedoids = None

        def add_function(self):#按钮绑定事件
            self.ui.k_mean_action.triggered.connect(lambda: self.k_mean_draw(self.add_fig_kmeans))
            self.ui.k_medoids_action.triggered.connect(lambda: self.k_medoids_draw(self.add_fig_KMedoids))
            # self.ui.actionMiniBatchKMeans.triggered.connect(lambda: self.k_mean_draw(MiniBatchKMeans,  self.add_fig_kmeans))
            self.ui.runButton_kMeans.clicked.connect(lambda: self.k_mean_draw(self.add_fig_kmeans))
            self.ui.runButton_KMedoids.clicked.connect(lambda: self.k_medoids_draw(self.add_fig_KMedoids))

            # self.ui.k_mean_action.triggered.connect(lambda: self.k_model_draw(KMeans, self.ui.plotWidget,self.add_fig_kmeans))
            # self.ui.k_medoids_action.triggered.connect(lambda: self.k_model_draw(KMedoids, self.ui.plotWidget,self.add_fig_KMedoids))
            # self.ui.actionMiniBatchKMeans.triggered.connect(lambda: self.k_model_draw(MiniBatchKMeans, self.ui.plotWidget,self.add_fig_kmeans))

            # self.ui.runButton_kMeans.clicked.connect(lambda: self.k_model_draw(KMeans, self.ui.plotWidget,self.add_fig_kmeans))
            # self.ui.runButton_KMedoids.clicked.connect(lambda: self.k_model_draw(KMedoids, self.ui.plotWidget,self.add_fig_KMedoids))

            self.ui.open_action.triggered.connect(self.open_data)
            self.ui.actionrandom.triggered.connect(self.setRandData)
            self.ui.randomButton.clicked.connect(self.setRandData)

        add_function(self)

    def open_data(self):#导入数据
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '',
                                                    'CSV files(*.csv )')  # QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls);;CSV files(*.csv )')
        print(openfile_name)
        if openfile_name[0] != '':
            self.data = datein((openfile_name[0]))
            self.add_datax_table()
            print("load ok")

    def add_fig_kmeans(self, fig):#画kmeans图
        if self.ui.plotWidget:
            self.layy.removeWidget(self.ui.plotWidget)
            self.ui.plotWidget.deleteLater()
            self.ui.plotWidget = None

        self.ui.plotWidget = FigureCanvas(fig)
        self.layy.addWidget(self.ui.plotWidget)
        print(self.layy.count())

    def add_fig_KMedoids(self, fig):#画KMedoids图
        if self.ui.plotWidget_KMedoids:
            self.layy_KMedoids.removeWidget(self.ui.plotWidget_KMedoids)
            self.ui.plotWidget_KMedoids.deleteLater()
            self.ui.plotWidget_KMedoids = None

        self.ui.plotWidget_KMedoids = FigureCanvas(fig)
        self.layy_KMedoids.addWidget(self.ui.plotWidget_KMedoids)
        print(self.layy_KMedoids.count())

    def k_medoids_draw(self, self_fig):#计算k_medoids
        # self.k_model_draw(KMeans)
        class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())
        max_iter_num = 300 if self.ui.lineEdit_max_iter.text() == "" else int(self.ui.lineEdit_max_iter.text())

        random_state = 170
        x_varied = self.data.x_varied

        if x_varied.shape[1] == 2:#2维数据
            fig, ax1 = plt.subplots(figsize=(8, 5))
        elif x_varied.shape[1] == 3:#3维数据
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')

        init_string = 'random' if self.ui.radioButton_kmedoids_random.isChecked() else 'heuristic' if self.ui.radioButton_kmedoids_heuristic.isChecked() else 'k-medoids++'

        # y_pred = KMedoids(n_clusters=class_num, random_state=random_state).fit_predict(x_varied)

        metric_string = self.ui.comboBox_kMedoids.currentText()
        print(metric_string)

        KMedoids_model = KMedoids(init=init_string, n_clusters=class_num, random_state=random_state,
                                  max_iter=max_iter_num, metric=metric_string)
        y_pred = KMedoids_model.fit_predict(self.data.x_varied)
        ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)

        global centroids
        centroids = None
        if self.ui.checkBox_Voronoi.isChecked():
            Vor_Dia(x_varied, KMedoids_model)
        self_fig(fig)
        self.evaluate(KMedoids_model, y_pred)

        self.add_datay_table(y_pred)

    def k_mean_draw(self, self_fig):#计算k_mean
        # self.k_model_draw(KMedoids)
        class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())#默认三类
        max_iter_num = 300 if self.ui.lineEdit_max_iter.text() == "" else int(self.ui.lineEdit_max_iter.text())#设置默认最大迭代次数
        n_init_num = 1 if self.ui.lineEdit_kmeans_runtimes.text() == "" else int(
            self.ui.lineEdit_kmeans_runtimes.text())

        random_state = 170
        x_varied = self.data.x_varied

        if x_varied.shape[1] == 2:#2维数据
            fig, ax1 = plt.subplots(figsize=(8, 5))
        elif x_varied.shape[1] == 3:#3维数据
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')

        init_string = 'random' if self.ui.radioButton_kmeans_random.isChecked() else 'k-means++'  # else 'heuristic' if self.ui.radioButton_kmeans_heuristic else 'k-means++'

        print(init_string)
        # y_pred = KMedoids(init=init_string,n_clusters=class_num, random_state=random_state,max_iter=max_iter_num).fit_predict(self.data.x_varied)
        KMeans_model = KMeans(init=init_string, n_init=n_init_num, n_clusters=class_num, random_state=random_state,
                              max_iter=max_iter_num)
        y_pred = KMeans_model.fit_predict(self.data.x_varied)
        ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)

        global centroids
        centroids = None
        if self.ui.checkBox_Voronoi.isChecked():
            centroids = Vor_Dia(x_varied, KMeans_model)
        self_fig(fig)
        self.evaluate(KMeans_model, y_pred)

        self.add_datay_table(y_pred)
    # def k_model_draw(self, func, plotWidget,self_fig):
    #     class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())
    #     max_iter_num = 300 if self.ui.lineEdit_max_iter.text() == "" else int(self.ui.class_num_lineEdit.text())
    #     fig, ax1 = plt.subplots(figsize=(8, 5))
    #     x_varied = self.data.x_varied
    #     y_pred = func(n_clusters=class_num, random_state=170).fit_predict(self.data.x_varied)
    #     ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)
    #     # self.add_fig_kmeans(fig)
    #     self_fig(fig)
    #     print(y_pred)
    #     print("drawOK")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
