'''input
3
11 2 4
4 5 6
10 8 -12
'''

n = int(raw_input())

left_sum =0
right_sum = 0

matrix = []
for i in range(n):
	line = map(int, raw_input().split())
	matrix.append(line)

for i in range(n):
	left_sum += matrix[i][i]

for i in range(n):
	right_sum += matrix[i][n-1-i]


print abs(left_sum - right_sum)


