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

x, y, z = coordinates[:, 0], coordinates[:, 1], coordinates[:, 2]
fig, axes = plt.subplots(1, 3, figsize=(20, 5))

# kmeans
kmeans = KMeans(n_clusters=5).fit(X_std)
axes[0] = plt.axes(projection ="3d")
axes[0].scatter3D(x, y, z, c=kmeans.labels_)

# gaussian mixture
gm = GaussianMixture(n_components=5, random_state=0).fit(X_std)
axes[1] = plt.axes(projection ="3d")
axes[1].scatter3D(x, y, z, c=gm.predict(X_std))

# clustering jerárquico
Z = linkage(X_std, 'ward')
clusters = fcluster(Z, t=126, criterion='distance')
axes[2] = plt.axes(projection ="3d")
axes[2].scatter3D(x, y, z, c=clusters)

plt.show()
