#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:16:13 2019

@author: tudou
"""
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np

n_samples = 1500
random_state = 170
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)

y_pred = KMedoids(n_clusters=3, metric='euclidean', random_state=random_state).fit_predict(X_varied)

plt.figure(figsize=(8, 5))
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")


#['euclidean', 'l2', 'l1', 'manhattan', 'cityblock',
# 'braycurtis', 'canberra', 'chebyshev',
# 'correlation', 'cosine', 'dice', 'hamming',134
# 'jaccard', 'kulsinski', 'mahalanobis', 'matching',123
# 'minkowski', 'rogerstanimoto', 'russellrao',
# 'seuclidean', 'sokalmichener', 'sokalsneath',
# 'sqeuclidean', 'yule', 'wminkowski',
# 'haversine']
#out_data=np.c_[X_varied,y_varied]
#pd.DataFrame(out_data).to_csv(index=False,path_or_buf='./p1.csv',header=None)
