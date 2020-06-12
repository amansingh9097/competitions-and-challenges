"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""
n, m = map(int,input().split())

for i in range(n//2):
	print(('.|.'*(2*i + 1)).center(m, '-'), sep="\n")

print('WELCOME'.center(m, '-'))

for i in range((n//2)-1, -1, -1):
	print(('.|.'*(2*i + 1)).center(m, '-'), sep="\n")
