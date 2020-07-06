"""
Write a function called sum_intervals() that accepts an array of intervals, and returns the sum of
all the interval lengths. Overlapping intervals should only be counted once.
"""

def sum_intervals (arr):
	arr.sort(key = lambda elem: elem[0])
	print(arr)
	if len(arr) == 0:
		return None
	global a, b, length
	a, b, total, length = 0, 0, 0, 0
	for i in range(len(arr) - 1):
		length = arr[i][1] - arr[i][0]
		if arr[i][1] < arr[i + 1][0]:
			# not overlapping
			if b - a != 0:
				length += (b - a)
				a, b = 0, 0
			total += length
		else:
			# e.g. [1,4],[3,5]
			if arr[i][1] < arr[i + 1][1]:
				a, b = arr[i][0], arr[i + 1][1]
			# e.g. [1,5],[3,4]
			else:
				b = arr[i][1]
	print(total)


test1 = [[1, 4],
		 [7, 10],
		 [3, 5]]
test2 = [[1, 2],
		 [6, 10],
		 [11, 15]]
test3 = [[1, 4],
		 [3, 5],
		 [7, 10], ]
test4 = [[1, 5],
		 [10, 20],
		 [1, 6],
		 [16, 19],
		 [5, 11]]

sum_intervals(test1)
sum_intervals(test2)
sum_intervals(test3)
sum_intervals(test4)
