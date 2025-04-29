import scipy.io
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Cargar los datos
mat_path = r"..\..\S03_datasets\coactivation_matrix\Coactivation_matrix.mat"
mat_data = scipy.io.loadmat(mat_path)

# Obtener la matriz de coactivación y las coordenadas
coactivation_matrix = mat_data['Coactivation_matrix']
coordinates = mat_data['Coord']

# Normalizando datos
X_std = StandardScaler().fit_transform(coactivation_matrix)


Z = linkage(X_std, 'ward')

clusters = fcluster(Z, t=126, criterion='distance')

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

x, y, z = coordinates[:, 0], coordinates[:, 1], coordinates[:, 2]
# Creating plot
ax.scatter3D(x, y, z, c=clusters, s=100)
plt.show()
