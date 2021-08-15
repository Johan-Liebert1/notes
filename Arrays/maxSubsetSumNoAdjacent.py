'''
find the max sum of subset of an array such that the elements are not adjacent
'''


def maxSum(array):
    new_array = [0] * len(array)

    new_array[0] = array[0]
    new_array[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        new_array[i] = max(new_array[i - 1], new_array[i - 2] + array[i])

    return new_array[-1]


print(maxSum([3, 64, 12, 32, 0, 91, 0, 0, 0, 1, 2, 3, 4, -64, 23, 1]))
