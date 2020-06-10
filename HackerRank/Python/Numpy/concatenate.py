"""
Task:
You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). 
Your task is to concatenate the arrays along axis 0.

Input Format:
The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format:
Print the concatenated array of size (N + M)xP.
"""
import numpy as np
n, m, _ = map(int, input().split())
arr1 = np.array([input().split() for _ in range(n)], dtype=int)
arr2 = np.array([input().split() for _ in range(m)], dtype=int)
print(np.concatenate((arr1, arr2), axis=0))