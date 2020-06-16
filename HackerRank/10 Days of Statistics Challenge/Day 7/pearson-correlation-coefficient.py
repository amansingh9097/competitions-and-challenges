def pearson_coef(X, Y, N):
	mean_X = sum(X) / len(X)
	mean_Y = sum(Y) / len(Y)

	std_X = (sum([(i - mean_X)**2 for i in X]) / len(X))**0.5
	std_Y = (sum([(i - mean_Y)**2 for i in Y]) / len(Y))**0.5

	return sum([(X[i] - mean_X)*(Y[i] - mean_Y) for i in range(N)]) / (N * std_X * std_Y)

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
print(round(pearson_coef(X, Y, N), 3))