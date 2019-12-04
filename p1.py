import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
# import pandas as pd
# import numpy as np

n_samples = 1500
random_state = 170

X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)

y_pred = KMeans(n_clusters=3, random_state=170).fit_predict(X_varied)

plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")

#out_data=np.c_[X_varied,y_varied]
#pd.DataFrame(out_data).to_csv(index=False,path_or_buf='./p1.csv',header=None)
print()