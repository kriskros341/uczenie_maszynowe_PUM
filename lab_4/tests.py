import numpy as np
from scipy import stats

x = np.array([179, 174, 181, 172, 116, 167, 103, 154, 123, 126, 161, 151, 100,
              143, 192])
y = np.array([185, 182, 195, 188, 139, 191, 131, 183, 164,  78, 210, 207, 160,
              76, 267])

print(stats.shapiro(x - y))
print(stats.ttest_rel(x, y))
print(stats.wilcoxon(x, y)) # obustronny
print(stats.wilcoxon(x, y, alternative='less')) # jednostronny
