def get_rank(X):
	x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
	return [x_rank[x] for x in X]

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rx = get_rank(X)
ry = get_rank(Y)

d = [(rx[i] - ry[i])**2 for i in range(n)]
rxy = 1 - (6 * sum(d)) / (n * (n**2 - 1))

print(round(rxy, 3))