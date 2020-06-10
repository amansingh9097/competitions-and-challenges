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
arr = sorted([int(a) for a in input().split()])
Q1, Q2, Q3 = quartiles(arr)
print(Q1)
print(Q2)
print(Q3)