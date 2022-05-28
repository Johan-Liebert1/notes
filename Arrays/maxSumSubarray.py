# kadane's algorithm

"""  
Using Dynamic Programming, keep track of the maximum sum at every index and then on the next index 
check if adding that element will increase the sum or not. Take the maximum of (adding the number to the max sum yet,
just the current number) -> this is to handle for negative numbers as it's better to take just 5 than to take (-9 + 5)
"""

# Time: O(n) | Space: O(n)
def maxSum(array):
    max_sum = array[0]
    max_sum_array = [0] * len(array)
    max_sum_array[0] = array[0]

    for i in range(1, len(array)):
        max_sum_array[i] = max(array[i] + max_sum_array[i - 1], array[i])
        max_sum = max(max_sum_array[i], max_sum)

    return max_sum


# Time: O(n) | Space: O(1)
def maxSubArray(self, array: list[int]) -> int:
    max_sum = array[0]
    prev_max = array[0]

    for i in range(1, len(array)):
        prev_max = max(array[i], array[i] + prev_max)

        if prev_max > max_sum:
            max_sum = prev_max

    return max_sum


print(maxSum([]))
