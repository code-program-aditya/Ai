"""Module providing a function printing python version."""

import numpy as np
from sklearn.cluster import KMeans

x = np.array([[1,2], [2,3], [3,3], [8,8], [9,8], [8,9]])
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(x)
print("cluster Labels:")
print(kmeans.labels_)
print("cluster Centers:")
print(kmeans.cluster_centers_)
