"""  
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 7
Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
Example 2:

Input: nums = [5,6,7,8]
Output: 8
Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
Example 3:

Input: nums = [6,2,1,2,4,5]
Output: 10
Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.
"""

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sum_even, sum_odd = 0, 0

        for i in range(len(nums)):
            temp_even = max(
                # including nums[i] in our sum, we add it to sum_odd as even indexed numbers are added
                sum_odd + nums[i],
                # not including nums[i], so we compare with sum even
                sum_even,
            )

            temp_odd = max(sum_even - nums[i], sum_odd)

            sum_even, sum_odd = temp_even, temp_odd

        # return sum_even as that will contain the sum starting from index 0, and sum odd
        # will contain sum starting from index 1 which we don't want as it's not the complete sum
        return sum_even

    def maxAlternatingSumRecursive(self, nums: List[int]) -> int:
        # cache[(index, even)] = something
        cache = {}

        def recurse(index, even):
            if (index, even) in cache:
                return cache[(index, even)]

            if index == len(nums):
                return 0

            total = nums[index] if even else -1 * nums[index]

            cache[(index, even)] = max(
                total + recurse(index + 1, not even), recurse(index + 1, even)
            )

            return cache[(index, even)]

        return recurse(0, True)
