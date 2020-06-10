def generate_arr(X, F):
	arr = []
	for i in range(len(X)):
		for j in range(F[i]):
			arr.append(X[i])
	return sorted(arr)

def median(arr):
	if len(arr)%2 == 0:
		return int(sum(arr[(len(arr)//2)-1:(len(arr)//2)+1])/2)
	else:
		return arr[len(arr)//2]

def quartiles(arr):
	Q1 = median(arr[:len(arr)//2])
	Q2 = median(arr)
	if n%2 == 0:
		Q3 = median(arr[len(arr)//2:])
	else:
		Q3 = median(arr[len(arr)//2+1:])
	return Q1,Q2,Q3

n = int(input())
X = [int(a) for a in input().split()]
F = [int(a) for a in input().split()]
arr = generate_arr(X, F)
Q1, Q2, Q3 = quartiles(arr)

print('{:.1f}'.format(Q3 - Q1))