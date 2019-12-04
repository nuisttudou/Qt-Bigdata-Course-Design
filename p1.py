import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
# import pandas as pd
import numpy as np

n_samples = 1500
random_state = 170

X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)
KMeans_model=KMeans(n_clusters=3, random_state=170)
y_pred = KMeans_model.fit_predict(X_varied)




#plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
#plt.title("Unequal Variance")

#out_data=np.c_[X_varied,y_varied]
#pd.DataFrame(out_data).to_csv(index=False,path_or_buf='./p1.csv',header=None)


h = .02
x_min, x_max = X_varied[:, 0].min() - 1, X_varied[:, 0].max() + 1
y_min, y_max = X_varied[:, 1].min() - 1, X_varied[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = KMeans_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
print()
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower'
           )
#plt.plot(X_varied[:, 0], X_varied[:, 1], 'k.', markersize=2)
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
# Plot the centroids as a white X
centroids = KMeans_model.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)




plt.show()