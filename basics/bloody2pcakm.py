import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score

## lab2_1
if __name__ == '__main__':
    fname = 'd01_frame_I300'
    #fname = 'd01_comparison_I350'
    record = np.load(f'{fname}.npz')
    
    data = record['data']
    X = np.reshape(data, (-1, data.shape[-1]))
    
    
    pca = PCA(n_components=10)
    Xdr = pca.fit_transform(X)

    n_clusters = 6
    clustering = KMeans(n_clusters=n_clusters).fit(Xdr)


    plt.figure('Clustering scatterplot')
    for i, label in enumerate(set(clustering.labels_)):
        index = clustering.labels_ == label
        color = plt.cm.tab10(label / (n_clusters - 1))
        plt.scatter(Xdr[index, 0], Xdr[index, 1], s=5, color=color, 
                    alpha=0.25, cmap=plt.cm.tab10)
    plt.xlabel('DR coordinate 1')
    plt.ylabel('DR coordinate 2')
    plt.title('Dimensionality reduction projection of X')
    plt.tight_layout()
    
    plt.figure('Clustering image')
    labels2 = np.reshape(clustering.labels_, data.shape[:2])
    plt.imshow(labels2, cmap=plt.cm.tab10)
    plt.tight_layout()
    plt.show()    
    