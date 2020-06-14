avg_A, avg_B = map(float, input().split())

cost_A = 160 + 40 * (avg_A + avg_A**2)
cost_B = 128 + 40 * (avg_B + avg_B**2)

print(round(cost_A, 3))
print(round(cost_B, 3))