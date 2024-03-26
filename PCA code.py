import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA

parameters_list = X = []

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

# perform PCA on data using both PCA from scratch and PCA from sklearn
data_skl, var_skl = by_sklearn(data, n_red)

# plot
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
fig.suptitle(f"{n}-D data as {n_red}-D data")

axs[1].scatter(data_skl[:,0],data_skl[:,1],color="r",s=1)
axs[1].set_title("Sklearn")
axs[1].set_xlabel(f"Variance: {round(var_skl[0],4)}")
axs[1].set_ylabel(f"Variance: {round(var_skl[1],4)}")

fig.tight_layout()
plt.show()