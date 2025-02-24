import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

if __name__ == '__main__':
    data = pd.read_csv('../data/wdbc.data', header=None).to_numpy()
    X = data[:, 2:]
    y = np.array(data[:, 1] == 'M', int)

    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Standardize features
        ('svm', SVC())                 # SVM classifier
    ])
    param_grid = {
        'svm__C': [0.01, 0.1, 1, 10, 100],
        'svm__gamma': [0.0001, 0.001, 0.01, 0.1, 1, 10],
        'svm__kernel': ['rbf']
    }
    grid_search = GridSearchCV(pipeline, param_grid, cv=5)
    skf = StratifiedKFold(n_splits=5)
    scores = cross_val_score(grid_search, X, y, cv=skf)
    grid_search.fit(X, y)
    
    print("Cross-validated scores:", scores)
    print("Average cross-validated score:", scores.mean())
