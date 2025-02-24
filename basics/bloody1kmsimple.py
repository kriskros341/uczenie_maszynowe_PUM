import numpy as np
from sklearn.cluster import KMeans


if __name__ == '__main__':
    fname = 'd01_frame_I300'
    #fname = 'd01_comparison_I350'
    record = np.load(f'{fname}.npz')
    
    data = record['data']
    X = np.reshape(data, (-1, data.shape[-1]))

    n_clusters = 5
    clustering = KMeans(n_clusters=n_clusters).fit(X)

    blood_label = int(input('Which cluster?'))
    result = clustering.labels_ == blood_label
    print(result)