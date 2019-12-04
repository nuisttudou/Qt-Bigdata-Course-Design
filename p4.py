import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,DBSCAN,MiniBatchKMeans,FeatureAgglomeration
from sklearn.datasets import make_blobs
import pandas as pd
# import numpy as np
# def all_model(func):
#     n_samples = 1500
#     random_state = 170
#
#     X_varied, y_varied = make_blobs(n_samples=n_samples,
#                                     cluster_std=[1.0, 2.5, 0.5],
#                                     random_state=random_state)
#
#     y_pred = func(n_clusters=3, random_state=0.1).fit_predict(X_varied)
#
#     plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
#     plt.title("Unequal Variance")
#
# all_model(MiniBatchKMeans)

n_samples = 1500
random_state = 170

X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)

y_pred = FeatureAgglomeration(n_clusters=3).fit(X_varied)

plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")
