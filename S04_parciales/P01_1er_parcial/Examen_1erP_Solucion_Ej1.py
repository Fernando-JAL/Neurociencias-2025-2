import os
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Se lee el dataset
path = r"..\..\S03_datasets\iris\iris.csv"
df = pd.read_csv(path)

# Se define el conjunto de datos
X = df.iloc[:, :4]

# Normalización de datos
media, sigma = X.mean(axis=0), X.std(axis=0)
X_std = (X - media)/sigma

X_std.describe()

# Cálculo de matriz de covarianza
cov_matrix = (X_std - X_std.mean(axis=0)).T.dot((X_std - X_std.mean(axis=0)))/(X_std.shape[0]-1)

# Cálculo de valores y vectores propios
eig_vals, eig_vectors = np.linalg.eig(cov_matrix)
# eig_vals, eig_vectors

# Cálculo de contribución por vector propio
eigen_pairs = [(np.abs(eig_vals[i]), eig_vectors[:,i]) for i in range(len(eig_vals))]

# Ordenamos de mayor a menor
eigen_pairs.sort(reverse=True)

# Calculamos los porcentajes
total_sum = sum(eig_vals)
var_exp = [(i/total_sum)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

# var_exp

print(f"""El porcentaje de información que 
se mantiene con 3 componentes principales 
es {np.round(cum_var_exp[2], 3)}%""")

T_matrix = np.stack((eigen_pairs[0][1],
                     eigen_pairs[1][1],
                     eigen_pairs[2][1]), axis=1)
# T_matrix

# Aquí calculamos los vectores proyectados sin usar for
Y = X_std.dot(T_matrix)
Y['Species'] = df['Species']
# Y
pca = PCA(n_components=3)
data_proyectada = pca.fit_transform(X_std)
# data_proyectada

fig = plt.figure(figsize=(5, 5))

ax = fig.add_subplot(111, projection='3d')
for idx, specie in enumerate(Y.Species.unique()):
    ax.scatter(Y[Y['Species'] == specie][0],
               Y[Y['Species'] == specie][1],
               Y[Y['Species'] == specie][2], s=40, label=specie)

ax.set_xlabel("CP 1")
ax.set_ylabel("CP 2")
ax.set_zlabel("CP 3")
plt.title('Dataset Iris con 3 componentes principales')

plt.legend(loc='best')
plt.show()

