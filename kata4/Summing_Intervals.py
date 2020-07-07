"""
Write a function called sum_intervals() that accepts an array of intervals, and returns the sum of
all the interval lengths. Overlapping intervals should only be counted once.
"""

# THIS IS INCORRECT!


def sum_intervals(arr):
    arr.sort(key=lambda elem: elem[0])
    print(arr)
    if len(arr) == 0:
        return None
    global total, length, a, b, sub
    total, length, a, b, sub = 0, 0, 0, 0, 0
    for i in range(len(arr)):
        length = arr[i][1] - arr[i][0]
        total += length
        # if overlapped
        if i != len(arr) - 1:
            if arr[i][1] > arr[i + 1][0]:
                # e.g. [1,4],[3,5]
                if arr[i][1] < arr[i + 1][1]:
                    sub = arr[i][1]-arr[i + 1][0]
                # e.g. [1,5],[3,4]
                else:
                    sub = arr[i+1][1] - arr[i+1][0]
                total -= sub
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
