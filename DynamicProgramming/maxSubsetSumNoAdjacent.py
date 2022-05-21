"""
find the max sum of subset of an array such that the elements are not adjacent
"""


def maxSum(array):
    new_array = [0] * len(array)

    new_array[0] = array[0]
    new_array[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        new_array[i] = max(new_array[i - 1], new_array[i - 2] + array[i])

    print(new_array)

    return new_array[-1]


def maxSumBetter(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    prev_prev, prev = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        prev_prev, prev = prev, max(prev, prev_prev + nums[i])

    return prev


# same as max sum, but now the first and last elements are also considered adjacent
def maxSumCircular(nums: list[int]) -> int:
    """
    3 options:
    include first but not last
    include last but not first
    don't include first or last

    dp from start to ignore last gives opportunity for option 1,
    dp after start to last gives opportunity for option 2,
    and both give opportunity for option 3
    """

    if len(nums) == 1:  # required, as default val of 0 might not exist
        return nums[0]

    a = b = c = d = 0
    for i, n in enumerate(nums):
        if i < len(nums) - 1:
            # not choosing the last one
            a, b = b, max(b, a + n)

        if i > 0:
            # not choosing the first one
            c, d = d, max(d, c + n)

    return max(b, d)


# print(maxSum([3, 64, 12, 32, 0, 91, 0, 0, 0, 1, 2, 3, 4, -64, 23, 1]))
print(maxSum([9, 6, -3, 4, 2, 1]))
