"""
Task:
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""

from itertools import permutations
S, k = input().split()
print(*[''.join(i) for i in permutations(sorted(S), int(k))], sep="\n")
# print("\n".join("".join(t) for t in sorted(list(permutations(S, int(k))))))