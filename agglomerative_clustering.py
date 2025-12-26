#creating dummy data
import pandas as pd
dummy = pd.read_csv('Amygdala_data.csv')
import numpy as np
from scipy.spatial import distance_matrix


#distance_matrix from scipy.spatial would calculate the distance between data point based on euclidean distance, and I round it to 2 decimal
print(pd.DataFrame(np.round(distance_matrix(dummy.values, dummy.values), 2), index = dummy.index, columns = dummy.index))

#importing linkage and denrogram from scipy
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt


#creating dendrogram based on the dummy data with single linkage criterion
den = dendrogram(linkage(dummy, method='single'),
labels = dummy.index)
plt.ylabel('Euclidean Distance', fontsize = 14)
plt.title('Dendrogram of Amygdala data')
plt.show()

from sklearn.cluster import AgglomerativeClustering
aglo = AgglomerativeClustering(n_clusters=2, linkage='complete', affinity='manhattan')
print(aglo.fit_predict(dummy))
dummy['Aglo-label'] = aglo.fit_predict(dummy)


print(dummy['Aglo-label'])
print(aglo.n_clusters_)





