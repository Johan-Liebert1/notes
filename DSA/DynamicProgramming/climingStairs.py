"""  
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        # start from the final one and start computing backwards
        # ways of reaching the nth step from nth step = 1
        # ways of reaching the nth setp from (n - 1)th step = 1 (+1 step, +2 overshoots)
        # ways of reaching the nth step from (n- 2)th step =
        # ways of reaching nth from nth + ways of reachin nth from (n-1)th

        for _ in range(n - 2, -1, -1):
            one, two = one + two, one

        return one

    def climbStairsDp(self, n: int) -> int:
        num = [None] * (n + 1)

        def steps(n):
            if num[n]:
                return num[n]

            if n in [0, 1, 2]:
                num[n] = n
                return num[n]

            num[n] = steps(n - 2) + steps(n - 1)
            return num[n]

        steps(n)

        return num[n]
