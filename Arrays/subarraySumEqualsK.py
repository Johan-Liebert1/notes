"""  
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


from typing import List


"""  
Maintain a prefix sum at every index in the array like, { prefix_sum: number_of_times_this_sum_occurs }

keep track of the cumulative sum until now in a variable s

at every point in the iteration, check if (s - k) is in prefix_sums dict. We want (s - k) as, if s (the cumulative sum)
is equal to 18 and k = 3, then if we find a prefix sum that is 15 (18 - 3) then removing that prefix will 
give us the sum of 3 which is what we want

We add a base case of 0 as the empty subarray having sum of 0. Because, if s = 3 and k = 3, then 3 - 3 = 0, but we might
not have 0 in out prefix sums and we will end up not counting this subarray
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sums = {0: 1}
        s = 0
        c = 0

        for i in nums:
            s += i

            if s - k in prefix_sums:
                c += prefix_sums[s - k]

            if s in prefix_sums:
                prefix_sums[s] += 1
            else:
                prefix_sums[s] = 1

        return c
