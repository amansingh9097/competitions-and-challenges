"""
Basically, the central limit theorem says, if X is a random variable that belongs 
to any distribution with mean 'μ' and standard deviation 'σ', 
then the sum of these random variables will converge to a 
'normal distribution' (provided n is big enough) with mean 'μ*σ' and standard deviation '√n*σ'.
"""

import math

X = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

sum_mu = n * mu
sum_sigma = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
	Z = (x - mu) / sigma
	return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(X, sum_mu, sum_sigma), 4))