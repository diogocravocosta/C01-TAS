import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA

from output_data_cleaner import get_output_airfoil_data

# rewriting airfoil coordinates to get only y values
xy_coordinates, latent_parameters = get_output_airfoil_data(False, 0)
y_coordinates = []
for i in range(0, len(xy_coordinates)):
    y_coordinates.append([])
    for j in range(0, len(xy_coordinates[i])):
        y_coordinates[i].append(xy_coordinates[i][j][1])

X = np.array(y_coordinates)
latent_parameters = np.array(latent_parameters)

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


def plot_scree():
    principal_components = [1,2,3,4,5,6,7,8,9,10]
    variances = []

    for i in range(1, 11):
        _, variance_ratio = by_sklearn(X, i)
        variances.append(variance_ratio[(i-1)])

    plt.plot(principal_components, variances, '-o', color='purple')
    plt.xlabel('Number of Principal Components')
    plt.xlabel('Variance Ratios')
    plt.show()

    return variances

# plot_scree()

pca_data, _ = by_sklearn(X, 8)


def compare(pc_n, lp_n):
    samples = list(range(1, 10002))

    pc = pca_data[:, (pc_n-1)]
    lp = latent_parameters[:, (lp_n-1)]

    plt.scatter(samples, pc, s=0.1, color='blue')
    plt.scatter(samples, lp, s=0.1, color='red')
    plt.show()

    return pc, lp

compare(6, 7)



# print(pca_data)
# print("========================================")
# print(latent_parameters)
#comment
