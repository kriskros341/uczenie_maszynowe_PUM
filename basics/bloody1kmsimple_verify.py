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
    return accuracy_score(result, blood)


if __name__ == '__main__':
    fname = 'd01_frame_I300'
    #fname = 'd01_comparison_I350'
    record = np.load(f'{fname}.npz')
    
    data = record['data']
    X = np.reshape(data, (-1, data.shape[-1]))

    n_clusters = 6
    clustering = KMeans(n_clusters=n_clusters).fit(X)

    best = 0
    besti = -1
    for label in range(n_clusters):
        result = clustering.labels_ == label
        val = verify(record, result)
        print(val)
        if val > best:
            best = val
            besti = label
    print(best)
    print(X[clustering.labels_ == besti])
    print(len(X[clustering.labels_ == besti]))

