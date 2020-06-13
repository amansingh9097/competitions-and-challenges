def factorial(n):
    return 1 if n == 0 else n*factorial(n - 1)

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def binomial(n, r, p):
    return combination(n, r) * pow(p, r) * pow(1 - p, n - r)

b, g = map(float, input().split())

result = round(sum([binomial(6, i, b/ (b + g)) for i in range(3, 7)]), 3)
print(result)