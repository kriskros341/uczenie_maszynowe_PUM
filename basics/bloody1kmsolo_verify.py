import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score



def verify(record, result):
    true_blood = record['anno'].ravel() == 1
    uncertain_blood = record['anno'].ravel() == 8
    blood = np.logical_or(true_blood, uncertain_blood)
    print(f'Accuracy {accuracy_score(result, blood):.2%}')


if __name__ == '__main__':
    fname = 'd01_frame_I300'
    #fname = 'd01_comparison_I350'
    record = np.load(f'{fname}.npz')
    
    data = record['data']
    X = np.reshape(data, (-1, data.shape[-1]))

    n_clusters = 6
    clustering = KMeans(n_clusters=n_clusters).fit(X)


    plt.figure(figsize=(8, 9))
    for i, label in enumerate(set(clustering.labels_)):
        index = clustering.labels_ == label
        Xlabel = X[index]
        print(f'Cluster {label} samples:', np.arange(len(X))[index])
        plt.subplot(321 + i)
        for x in Xlabel:
            plt.plot(x / np.max(x), '-', lw=2, alpha=0.75, color='rbgycmk'[label])
        plt.xlabel('Frequency index')
        plt.ylabel('Normalized reflectance')
        plt.title(f'Cluster {label}, size {np.count_nonzero(index)}')
    plt.tight_layout()
    plt.show()

    blood_label = int(input('Which cluster?'))
    result = clustering.labels_ == blood_label

    verify(record, result)
