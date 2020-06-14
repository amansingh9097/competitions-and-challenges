import math
mean, std = map(int, input().split())
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2**0.5))))

q1 = int(input())
print(round((1-cdf(q1))*100, 2))
q2 = int(input())
print(round((1-cdf(q2))*100, 2))
print(round((cdf(q2))*100, 2))