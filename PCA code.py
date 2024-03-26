import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA

from output_data_cleaner import get_output_airfoil_data

_, unsorted_lps = get_output_airfoil_data(False, 0)

def n_parameters_list (n1, n2, n3, n4, n5): # n1 is the first latent parameter you wanna look at, n2 is the second one you wanna compare
    return [[data_point[n1], data_point[n2], data_point[n3], data_point[n4], data_point[n5]] for data_point in unsorted_lps][1:]

X = np.array(n_parameters_list(0,1,2,3,4))
X2 = np.array(n_parameters_list(3,4,5,6,7))

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
data_skl, var_skl = by_sklearn(X, 2)
data_skl2, var_skl2 = by_sklearn(X2, 2)


# plot
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
# fig.suptitle(f"{n}-D data as {n_red}-D data")

# x_values, y_values = zip(*n_parameters_list(0,1))
# axs[0].scatter(x_values, y_values, color='b', s=0.5)
# x_values2, y_values2 = zip(*n_parameters_list(0,2))
# axs[1].scatter(x_values2, y_values2, color='b', s=0.5)

axs[0].scatter(data_skl[:,0],data_skl[:,1],color="r",s=1)
axs[0].set_title("Sklearn")
axs[0].set_xlabel(f"Variance: {round(var_skl[0],4)}")
axs[0].set_ylabel(f"Variance: {round(var_skl[1],4)}")

axs[1].scatter(data_skl2[:,0],data_skl2[:,1],color="green",s=1)
axs[1].set_title("Sklearn")
axs[1].set_xlabel(f"Variance: {round(var_skl2[0],4)}")
axs[1].set_ylabel(f"Variance: {round(var_skl2[1],4)}")

fig.tight_layout()
plt.show()