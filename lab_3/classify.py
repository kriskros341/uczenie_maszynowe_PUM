import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split


def loader(fname):
    record = np.load(fname, allow_pickle=True)
    return record['X'], record['y']


def test(clf, fname='test0.npz'):
    X_test, y_test = loader('test.npz') 
    y_predict = clf.predict(X_test)
    a = accuracy_score(y_test, y_predict)
    print(f'accuracy = {a:.2%}')



if __name__ == '__main__':
    X, Y = loader('train.npz')

    clf = KNeighborsClassifier(n_neighbors=20)
    clf.fit(X, Y)
    print()

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    test(clf)
