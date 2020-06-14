from math import exp, factorial

def poisson_dist_prob(k, lambda_):
	return (lambda_**k * exp(-lambda_))/factorial(k)

l = float(input())
k = int(input())
print(round(poisson_dist_prob(k, l),3))