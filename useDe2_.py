from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvas

from sklearn import metrics
from de2 import Ui_MainWindow  # importing our generated file
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs
import pandas as pd
from sklearn_extra.cluster import KMedoids
import random
from Voronoi_Diagram_ import *


def he():
    print("test")


class datein():
    def __init__(self, pwd=""):
        if pwd == "":
            return
        da = np.array(pd.read_csv(pwd))
        self.x_varied, self.y_varied = da[:, 0:2], da[:, 2]

    # print(self.x_varied.shape)
    # print(self.x_varied)
    # def __init__(self):
    #     n_samples = 1500
    #     self.x_varied, self.y_varied= make_blobs(n_samples=n_samples,cluster_std=[1.0, 2.5, 0.5])


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def evaluate(self, model, y_pred, ):
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

        eva_string = "homo:" + str(metrics.homogeneity_score(y_pred, self.data.y_varied)) + '\t' + \
                     "compl:" + str(metrics.completeness_score(y_pred, self.data.y_varied)) + '\t' + \
                     "v-meas:" + str(metrics.v_measure_score(y_pred, self.data.y_varied)) + '\t' + \
                     "ARI:" + str(metrics.adjusted_rand_score(y_pred, self.data.y_varied)) + '\t' + \
                     "AMI:" + str(metrics.adjusted_mutual_info_score(y_pred, self.data.y_varied))
        self.ui.label_evaluat.setText(eva_string)

    def setRandData(self):
        self.data = datein()
        centers_num = int(self.ui.horizontalSlider.value())
        cluster_std_ = [random.random() for _ in range(centers_num)]
        self.data.x_varied, self.data.y_varied = make_blobs(n_samples=1500, cluster_std=cluster_std_,
                                                            centers=centers_num)  # , cluster_std=[1.0, 2.5, 0.5])
        print("random OK")

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.add_function()
        self.data = None

        self.layy = QtWidgets.QVBoxLayout(self.ui.kmeans_content_plot)
        self.ui.plotWidget = None

        self.layy_KMedoids = QtWidgets.QVBoxLayout(self.ui.kmedoids_content_plot)
        self.ui.plotWidget_KMedoids = None

    def add_function(self):
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

    def open_data(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls);;CSV files(*.csv )')
        print(openfile_name)
        if openfile_name[0] != '':
            self.data = datein((openfile_name[0]))
            print("load ok")

    def add_fig_kmeans(self, fig):
        if self.ui.plotWidget:
            self.layy.removeWidget(self.ui.plotWidget)
            self.ui.plotWidget.deleteLater()
            self.ui.plotWidget = None

        self.ui.plotWidget = FigureCanvas(fig)
        self.layy.addWidget(self.ui.plotWidget)
        print(self.layy.count())

    def add_fig_KMedoids(self, fig):
        if self.ui.plotWidget_KMedoids:
            self.layy_KMedoids.removeWidget(self.ui.plotWidget_KMedoids)
            self.ui.plotWidget_KMedoids.deleteLater()
            self.ui.plotWidget_KMedoids = None

        self.ui.plotWidget_KMedoids = FigureCanvas(fig)
        self.layy_KMedoids.addWidget(self.ui.plotWidget_KMedoids)
        print(self.layy_KMedoids.count())

    def k_medoids_draw(self, self_fig):
        # self.k_model_draw(KMeans)
        class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())
        max_iter_num = 300 if self.ui.lineEdit_max_iter.text() == "" else int(self.ui.lineEdit_max_iter.text())
        fig, ax1 = plt.subplots(figsize=(8, 5))

        init_string = 'random' if self.ui.radioButton_kmedoids_random.isChecked() else 'heuristic' if self.ui.radioButton_kmedoids_heuristic.isChecked() else 'k-medoids++'
        random_state = 170
        x_varied = self.data.x_varied
        # y_pred = KMedoids(n_clusters=class_num, random_state=random_state).fit_predict(x_varied)

        metric_string = self.ui.comboBox_kMedoids.currentText()
        print(metric_string)

        KMedoids_model = KMedoids(init=init_string, n_clusters=class_num, random_state=random_state,
                                  max_iter=max_iter_num, metric=metric_string)
        y_pred = KMedoids_model.fit_predict(self.data.x_varied)
        ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)
        if self.ui.checkBox_Voronoi.isChecked():
            Vor_Dia(x_varied, KMedoids_model)
        self_fig(fig)
        self.evaluate(KMedoids_model, y_pred)

    def k_mean_draw(self, self_fig):
        # self.k_model_draw(KMedoids)
        class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())
        max_iter_num = 300 if self.ui.lineEdit_max_iter.text() == "" else int(self.ui.lineEdit_max_iter.text())
        n_init_num = 1 if self.ui.lineEdit_kmeans_runtimes.text() == "" else int(
            self.ui.lineEdit_kmeans_runtimes.text())
        fig, ax1 = plt.subplots(figsize=(8, 5))

        random_state = 170
        x_varied = self.data.x_varied

        init_string = 'random' if self.ui.radioButton_kmeans_random.isChecked() else 'k-means++'  # else 'heuristic' if self.ui.radioButton_kmeans_heuristic else 'k-means++'

        print(init_string)
        # y_pred = KMedoids(init=init_string,n_clusters=class_num, random_state=random_state,max_iter=max_iter_num).fit_predict(self.data.x_varied)
        KMeans_model = KMeans(init=init_string, n_init=n_init_num, n_clusters=class_num, random_state=random_state,
                              max_iter=max_iter_num)
        y_pred = KMeans_model.fit_predict(self.data.x_varied)
        ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)
        if self.ui.checkBox_Voronoi.isChecked():
            Vor_Dia(x_varied, KMeans_model)
        self_fig(fig)
        self.evaluate(KMeans_model, y_pred)
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
