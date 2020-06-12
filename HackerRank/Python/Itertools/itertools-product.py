"""
Task:
You are given a two lists A and B. Your task is to compute their cartesian product A x B.

Example:
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Basically, product(A, B) returns the same as ((x,y) for x in A for y in B)

Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format:
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.
"""

from itertools import product

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
print(*product(A,B))  # [print(t, end=" ") for t in list(product(A, B))]