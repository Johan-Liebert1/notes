"""  
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.
 

Example 1:

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
"""


from typing import List


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        max_area = 0
        max_area_height = 0
        prev = 0

        for i in range(len(horizontalCuts)):
            current_area = w * (horizontalCuts[i] - prev)

            if current_area >= max_area:
                max_area = current_area
                max_area_height = horizontalCuts[i] - prev

            prev = horizontalCuts[i]

        current_area = w * (h - horizontalCuts[-1])

        if current_area >= max_area:
            max_area = current_area
            max_area_height = h - horizontalCuts[-1]

        prev = 0
        max_left = 0

        for i in range(len(verticalCuts)):
            x = verticalCuts[i] - prev

            left = x * max_area_height
            right = max_area - left

            if left > max_left:
                max_left = left

            max_area = max(left, right, max_left)

            prev = verticalCuts[i]

        return max_area % 1000000007
