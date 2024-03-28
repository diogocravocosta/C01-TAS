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

principal_components = [1,2,3,4,5,6,7,8,9,10]
variances = []

for i in range(1, 11):
    _, variance_ratio = by_sklearn(X, i)
    variances.append(variance_ratio[(i-1)])

print(variances)

plt.plot(principal_components, variances, '-o', color='purple')
plt.show()