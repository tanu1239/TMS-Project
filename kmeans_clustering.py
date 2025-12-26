from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

X = pd.read_csv('Amygdala_data.csv')

kmeans = KMeans(n_clusters=5).fit(X)

print(kmeans.cluster_centers_)
print(kmeans.labels_)







