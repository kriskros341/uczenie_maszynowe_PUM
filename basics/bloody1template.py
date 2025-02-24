import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la
from sklearn.decomposition import PCA

X = np.load('blood1X.npz')['X']
pca = PCA(n_components=2)
Xpca = pca.fit_transform(X)
# with pca, the anomalies tend to be pushed fuhrther
distance = [la.norm(x) for x in Xpca.T[1]]
furthest = np.argsort(distance)[-1]
np.savez_compressed('blood_template.npz', template=X[furthest])

plt.scatter(Xpca.T[0], Xpca.T[1])
plt.show()

for x in np.argsort(distance)[::-1][:3]:
    plt.plot(X[x], 'k-')
    plt.xlabel('Wavelength index')
    plt.ylabel('Reflectance')
    plt.title('Template for inspection')
    plt.tight_layout()
plt.show()
