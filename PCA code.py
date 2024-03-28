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

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
# fig.suptitle(f"{n}-D data as {n_red}-D data")
# x_values, y_values = zip(*n_parameters_list(0,1))
# axs[0].scatter(x_values, y_values, color='b', s=0.5)
# x_values2, y_values2 = zip(*n_parameters_list(0,2))
# axs[1].scatter(x_values2, y_values2, color='b', s=0.5)

# axs[0].scatter(data_skl[:,0],data_skl[:,1],color="r",s=1)
# axs[0].set_title("latent parameters 1-5")
# axs[0].set_xlabel(f"Variance: {round(var_skl[0],4)}")
# axs[0].set_ylabel(f"Variance: {round(var_skl[1],4)}")
#
# axs[1].scatter(data_skl2[:,0],data_skl2[:,1],color="green",s=1)
# axs[1].set_title("latent parameters 4-8")
# axs[1].set_xlabel(f"Variance: {round(var_skl2[0],4)}")
# axs[1].set_ylabel(f"Variance: {round(var_skl2[1],4)}")
#
# fig.tight_layout()
# plt.show()