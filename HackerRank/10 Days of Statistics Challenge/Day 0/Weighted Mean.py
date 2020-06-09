n = int(input())
X = [int(i) for i in input().split()]
W = [int(i) for i in input().split()]

print(round(sum([a*b for a,b in zip(X,W)]) / sum(W), 1))