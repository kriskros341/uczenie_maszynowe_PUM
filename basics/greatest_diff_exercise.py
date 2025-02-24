from sklearn.ensemble import IsolationForest
import numpy as np

X = np.load('d01_comparison_I350.npz')['X']
print(X)
best = 0
best_labels = 0

results = []
ifor = IsolationForest().fit(X)
iforScores = ifor.score_samples(X)
iforScoresSortedIndexes = np.argsort(iforScores)

def findBiggestDiff(sortedScores):
    best_i = -1
    best_val = 0
    for i in range(1, len(sortedScores)):
        val = abs(abs(sortedScores[i]) - abs(sortedScores[i-1]))
        if best_val < val:
            best_i = i
            best_val = val
    return best_i

cutoff = findBiggestDiff(iforScores[iforScoresSortedIndexes])

print(cutoff)
print(iforScoresSortedIndexes[:cutoff])
