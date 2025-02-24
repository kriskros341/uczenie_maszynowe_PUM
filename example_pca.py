import numpy as np
import matplotlib.pyplot as plt

import scipy.linalg as la # filtrowanie, optymalizacje
from sklearn.decomposition import PCA


X = np.load('blood2X.npz')['X']

pca = PCA(n_components=2)
Xpca = pca.fit_transform(X)


distance = [la.norm(x) for x in Xpca]
print(np.argsort(distance)[::-1])


display = [37, 107, 28, 118, 14]
plt.figure(figsize=(5, 10))
for i_plot, i_dist in enumerate(display):
    plt.subplot(5, 2, 1 + 2*i_plot)
    plt.plot(X[i_dist], 'k-', lw=2)
    plt.xlabel('Frequency index')
    plt.ylabel('Normalized reflectance')
    plt.title(f'Sample {i_dist}, distance {distance[i_dist]:.3f}')
    plt.subplot(5, 2, 1 + 2*i_plot + 1)
    plt.scatter(Xpca[:, 0], Xpca[:, 1], c='k', alpha=0.5)
    plt.scatter([Xpca[i_dist, 0]], [Xpca[i_dist, 1]], c='r')
    plt.xlabel('PCA coordinate 1')
    plt.ylabel('PCA coordinate 2')
    plt.title('PCA projection of X')
plt.tight_layout()
plt.show()