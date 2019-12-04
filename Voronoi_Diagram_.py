import numpy as np
import matplotlib.pyplot as plt

def Vor_Dia(X_varied,model):
    centroids = model.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=40, linewidths=1,
                color='b', zorder=10)

    h = .02
    x_min, x_max = X_varied[:, 0].min() - 1, X_varied[:, 0].max() + 1
    y_min, y_max = X_varied[:, 1].min() - 1, X_varied[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print()
    # plt.figure(1)
    # plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower'
               )