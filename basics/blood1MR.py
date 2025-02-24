import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.ensemble import IsolationForest



X = np.load('blood2X.npz')['X']

# Standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensionality
pca = sklearnPCA(n_components=2)  # Reduce to 2 dimensions for visualization and effective anomaly detection
X_pca = pca.fit_transform(X_scaled)

# Apply Isolation Forest again on the PCA-transformed data
iso_forest_pca = IsolationForest(n_estimators=100, contamination=3/123, random_state=42)
iso_forest_pca.fit(X_pca)
anomalies_pca = iso_forest_pca.predict(X_pca)

# Find the indices of anomalies after PCA transformation
indices_anomalies_pca = np.where(anomalies_pca == -1)[0]

# Scatter plot of the PCA-transformed dimensions, highlighting anomalies
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', label='Normal Samples', edgecolor='k')
plt.scatter(X_pca[indices_anomalies_pca, 0], X_pca[indices_anomalies_pca, 1], c='red', label='Anomalies (Substancja1)', edgecolor='k')
plt.title('PCA-Transformed Samples with Anomalies Highlighted')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
#print(sorted(X_pca, key=lambda i: X_pca[i, 1]))
plt.show()
