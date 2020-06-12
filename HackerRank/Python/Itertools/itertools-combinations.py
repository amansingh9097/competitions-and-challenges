"""
You are given a string .
Your task is to print all 
possible combinations, up to size , of the string in lexicographic sorted order.
"""
from itertools import combinations
S, k = input().split()
for i in range(1, int(k)+1):
	for j in combinations(sorted(S), i):
		print("".join(j))