import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA

from output_data_cleaner import get_output_airfoil_data

# rewriting airfoil coordinates to get only y values
xy_coordinates, _ = get_output_airfoil_data(False, 0)
y_coordinates = []
for i in range(0, len(xy_coordinates)):
    y_coordinates.append([])
    for j in range(0, len(xy_coordinates[i])):
        y_coordinates[i].append(xy_coordinates[i][j][1])

X = np.array(y_coordinates)

def by_sklearn(X:np.array, k:int):

    # standardize data
    X_stand = preprocessing.StandardScaler().fit_transform(X)

    # perform PCA
    pca = PCA(k)

    # project data on principal axes
    new_data = pca.fit_transform(X_stand)

    # obtain variances
    variances = pca.explained_variance_ratio_

    return new_data, variances

# perform PCA on data using PCA from sklearn
data_skl, var_skl = by_sklearn(X, 8)


# NO POINT IN PLOTTING 8 DIMENSIONS

# fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
#
# PC_values = np.arange(pca.n_components_) + 1
# plt.plot(PC_values, pca.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
# plt.title('Scree Plot')
# plt.xlabel('Principal Component')
# plt.ylabel('Variance Explained')
# plt.show()
#test