""" Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3 """


from typing import List


_ = """  
this can be thought of as a linked list cycle detection problem.
Considering each index of the array as the pointer to the next node, there will 
be one index that will be pointed to more than once (as there is a repeated number and we are 
Considering indicies as pointers) 

 0  1  2  3  4
[1, 3, 4, 2, 2]

(index, value)
(0, 1) -> (1, 3) -> (3, 2) -> (2, 4) -> (4, 2) ->
                                ^               |
                                |               v
                                ----------------  

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # similar to the linked list cycle detection problem
        p1 = 0
        p2 = 0

        while 1:
            p1 = nums[p1]
            p2 = nums[nums[p2]]

            if p1 == p2:
                break

        slow = 0

        while p1 != slow:
            slow = nums[slow]
            p2 = nums[p2]

        return nums[slow]


s = Solution()
s.findDuplicate([1, 3, 4, 2, 2])
