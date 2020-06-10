"""
Task:
Read an integer N. For all non-negative integers i < N, print i^2. See the sample for details.
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(21):
    	if i < n:
    		print(i**2)