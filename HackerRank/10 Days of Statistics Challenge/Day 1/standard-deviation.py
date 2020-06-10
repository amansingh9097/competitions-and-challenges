from math import sqrt
n = int(input())
arr = [int(x) for x in input().split()]

mean = sum(arr) / n
variance = sum([(x - mean) ** 2 for x in arr]) / n
std = variance ** 0.5

print('{:.1f}'.format(std))