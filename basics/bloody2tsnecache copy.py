import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score
from sklearn.cluster import AgglomerativeClustering


if __name__ == '__main__':
    fname = 'd01_frame_I300'
    #fname = 'd01_comparison_I350'
    record = np.load(f'{fname}.npz')
    
    data = record['data']
    X = np.reshape(data, (-1, data.shape[-1]))
    import os
    
    #pca = PCA(n_components=10)
    file_path = 'tsne_results.txt'
    #Xdr = pca.fit_transform(X)
    if os.path.exists(file_path):
        print("Plik istnieje.")
        pca = np.loadtxt(file_path)
    else:
        pca = TSNE(n_components=2).fit_transform(X)
    
        # Zapisz wyniki do pliku tekstowego
        np.savetxt('tsne_results.txt', pca)

    n_clusters = 4

    clustering = AgglomerativeClustering(linkage='single').fit(X)

    plt.figure('Clustering scatterplot')
    for i, label in enumerate(set(clustering.labels_)):
        index = clustering.labels_ == label
        color = plt.cm.tab10(label / (n_clusters - 1))
        plt.scatter(pca[index, 0], pca[index, 1], s=5, c=color, 
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
    