"""  
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        table = {}

        for t in time:
            key = t % 60

            if key not in table:
                table[key] = 0

            table[key] += 1

        pairs = 0

        # 0 and 30 are special cases as they form pairs with each other and can only
        # form pairs if their count is greater than 1
        # dividing by 2 to prevent duplicate counting
        if table.get(0) is not None:
            pairs += ((table[0] - 1) * table[0]) / 2

        if table.get(30) is not None:
            pairs += ((table[30] - 1) * table[30]) / 2

        for key, value in table.items():
            if key == 0 or key >= 30:
                # to prevent duplicates and 0 and 30 are special cases
                continue

            if table.get(60 - key) is not None:
                # if there are 2 20's and 3 40's, we can make 2 * 3 = 6 pairs with them
                pairs += value * table[60 - key]

        return int(pairs)

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # variantion of 2 sum
        c = [0] * 60
        res = 0

        for t in time:
            res += c[(60 - t % 60) % 60]  # take care of 60
            c[t % 60] += 1

        return res
