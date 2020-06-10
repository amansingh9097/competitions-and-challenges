"""
Task:
Your task is to print an array of size MxN with its main diagonal elements as 1's and 0's everywhere else.
"""
import numpy as np

m, n = map(int, input().split())
print(str(np.eye(m,n)).replace('1',' 1').replace('0',' 0'))