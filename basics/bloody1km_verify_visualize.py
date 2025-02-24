import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la
from sklearn.cluster import DBSCAN
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
    
    xt = np.load('blood_template.npz')['template']
    n_clusters = 11
    clustering = DBSCAN(eps=0.2, min_samples=5).fit(X)
    
    label_errors = []
    for i, label in enumerate(set(clustering.labels_)):
        index = clustering.labels_ == label
        Xlabel = X[index]
        errors = [la.norm(x / np.max(x) - xt) for x in Xlabel]
        print(f'Cluster {i}, length {np.count_nonzero(index)}, mean {np.mean(errors)}')
        label_errors.append(np.mean(errors))
    
    label_with_minimum_error = np.argmin(label_errors)
    result = clustering.labels_ == label_with_minimum_error
    print(f'Minimum error in label {label_with_minimum_error}')
    
    verify(record, result)
    
    plt.figure('All labels')
    labels2 = np.reshape(clustering.labels_, data.shape[:2])
    plt.imshow(labels2, cmap=plt.cm.tab10)
    
    plt.figure('Results')
    result2 = np.reshape(result, data.shape[:2])
    plt.imshow(result2, cmap=plt.cm.tab10)
    plt.show()
