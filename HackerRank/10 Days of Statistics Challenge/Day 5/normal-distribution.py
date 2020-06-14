import math
mean, std = map(int, input().split())
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2**0.5))))

q1 = float(input()) # value for question 1
print(round(cdf(q1), 3))

q2_1, q2_2 = map(float, input().split()) # values for question 2
print(round(cdf(q2_2) - cdf(q2_1), 3))