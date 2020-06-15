import math

X = int(input())
n = int(input())
mu = float(input())
sigma = float(input())

sum_mu = n * mu
sum_sigma = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
	Z = (x - mu) / sigma
	return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(X, sum_mu, sum_sigma), 4))