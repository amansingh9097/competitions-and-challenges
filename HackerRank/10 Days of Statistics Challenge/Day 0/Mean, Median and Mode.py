import numpy as np
from scipy.stats import mode

n = int(input())
arr = [int(i) for i in input().split()]
print(np.mean(arr))
print(np.median(arr))
print(int(mode(arr)[0]))