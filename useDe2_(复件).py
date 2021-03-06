from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvas
from de2 import Ui_MainWindow  # importing our generated file
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd
from sklearn_extra.cluster import KMedoids


def he():
    print("test")

class datein():
    def __init__(self, pwd=""):
        if pwd=="":
            return
        da = np.array(pd.read_csv(pwd))
        self.x_varied, self.y_varied = da[:, 0:2], da[:, 2]

    # print(self.x_varied.shape)
    # print(self.x_varied)
    # def __init__(self):
    #     n_samples = 1500
    #     self.x_varied, self.y_varied= make_blobs(n_samples=n_samples,cluster_std=[1.0, 2.5, 0.5])
class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def setRandData(self):
        self.data = datein()
        self.data.x_varied, self.data.y_varied = make_blobs(n_samples=1500, cluster_std=[1.0, 2.5, 0.5])
        print("random OK")

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.add_function()
        self.data = None

        self.layy = QtWidgets.QVBoxLayout(self.ui.content_plot)
        self.ui.plotWidget = None

    def add_function(self):
        # self.ui.runButton.clicked.connect(self.draw)
        self.ui.k_mean_action.triggered.connect(self.k_mean_draw)
        self.ui.k_medoids_action.triggered.connect(self.k_medoids_draw)
        self.ui.open_action.triggered.connect(self.open_data)
        self.ui.actionrandom.triggered.connect(self.setRandData)

    def open_data(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls);;CSV files(*.csv )')
        print(openfile_name)
        if openfile_name[0] != '':
            self.data = datein((openfile_name[0]))
            print("load ok")

    def add_fig(self,fig):
        if self.ui.plotWidget:
            self.layy.removeWidget(self.ui.plotWidget)
            self.ui.plotWidget.deleteLater()
            self.ui.plotWidget=None

        self.ui.plotWidget = FigureCanvas(fig)
        self.layy.addWidget(self.ui.plotWidget)
        print(self.layy.count())

    def k_medoids_draw(self):
        class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())
        fig, ax1 = plt.subplots(figsize=(8, 5))
        # n_samples = 1500
        random_state = 170
        x_varied = self.data.x_varied
        y_pred = KMeans(n_clusters=class_num, random_state=random_state).fit_predict(x_varied)
        ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)
        self.add_fig(fig)

    def k_mean_draw(self):
        class_num = 3 if self.ui.class_num_lineEdit.text() == "" else int(self.ui.class_num_lineEdit.text())
        fig, ax1 = plt.subplots(figsize=(8, 5))
        # n_samples = 1500
        random_state = 170
        x_varied = self.data.x_varied
        y_pred = KMedoids(n_clusters=class_num, random_state=random_state).fit_predict(self.data.x_varied)
        ax1.scatter(x_varied[:, 0], x_varied[:, 1], c=y_pred)
        print(y_pred)
        self.add_fig(fig)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
