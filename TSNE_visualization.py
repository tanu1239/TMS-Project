import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Amygdalamni.csv')
print(data.shape)

#3d graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data.iloc[:, 0], data.iloc[:, 1], data.iloc[:, 2], c='r', marker='o')
plt.show()
#actual tsne visualization
tsne = TSNE(n_components = 2, perplexity = 50, learning_rate = 500)
data_2d = tsne.fit_transform(data)
plt.scatter(data_2d[:, 0], data_2d[:, 1])
plt.show()
#
