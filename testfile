import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#data set structured with 8 parameters as columns
df = pd.read_dat('organizeddataset.data')

# Selecting only the 8-dimensional parameters for PCA
# Replace 'param1', 'param2', ..., 'param8' with your actual parameter column names
X = df[['param1', 'param2', 'param3', 'param4', 'param5', 'param6', 'param7', 'param8']]

# Standardizing the features (important for PCA)
X_standardized = StandardScaler().fit_transform(X)

# Performing PCA
pca = PCA(n_components=2)  # We reduce the data to 2 dimensions for visualization
principalComponents = pca.fit_transform(X_standardized)

# Creating a DataFrame with the principal components
principalDf = pd.DataFrame(data=principalComponents, columns=['Principal Component 1', 'Principal Component 2'])

# Visualizing the principal components
plt.figure(figsize=(8, 6))
plt.scatter(principalDf['Principal Component 1'], principalDf['Principal Component 2'])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('2D PCA')
plt.show()

# Displaying explained variance ratio
print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")