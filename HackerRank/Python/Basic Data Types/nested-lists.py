"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and 
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, 
and the second line contains their grade.

Constraints:
2 <= N <= 5
There will always be one or more students having the second lowest grade.
"""

if __name__ == '__main__':
	marksheet = []
	for _ in range(int(input())):
		marksheet.append([input(), float(input())])

	second_highest_mark = sorted(set([mark for name, mark in marksheet]))[1]
	print('\n'.join(sorted([name for name, mark in marksheet if mark==second_highest_mark])))