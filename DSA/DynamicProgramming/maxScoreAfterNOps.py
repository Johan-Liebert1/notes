"""  
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
"""


from functools import lru_cache
import math
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        g = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                g[i][j] = math.gcd(nums[i], nums[j])

        @lru_cache(None)
        def recurse(iteration, mask):
            if mask == 0:
                # every element has been used
                return 0

            best = 0

            for x in range(n):
                if (mask & (1 << x)) > 0:
                    for y in range(x + 1, n):
                        if (mask & (1 << y)) > 0:
                            score = (
                                iteration * g[x][y]
                                +
                                # the maxk has to be XOR. Cannot use an OR mask
                                recurse(iteration + 1, mask ^ (1 << x) ^ (1 << y))
                            )

                            if score > best:
                                best = score

            return best

        return recurse(1, (1 << n) - 1)
