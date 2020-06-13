def factorial(n):
    return 1 if n == 0 else n*factorial(n - 1)

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def binomial(n, r, p):
    return combination(n, r) * p**r * (1 - p)**(n - r)

a, b = map(int, input().split())

print(round(sum([binomial(b, i, a/100) for i in range(3)]), 3))
print(round(sum([binomial(b, i, a/100) for i in range(2, b+1)]), 3))