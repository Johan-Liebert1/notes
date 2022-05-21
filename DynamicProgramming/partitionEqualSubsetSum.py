"""  
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        summ = sum(nums)

        if summ % 2 == 1:
            return False

        target = summ // 2
        cache = set([0])

        for i in range(len(nums)):
            next_cache = set()

            for t in cache:
                if t + nums[i] == target:
                    return True

                # not taking nums[i] in the subset sum
                next_cache.add(t)
                # taking nums[i] in the subset sum
                next_cache.add(t + nums[i])

            cache = next_cache

        return target in cache
