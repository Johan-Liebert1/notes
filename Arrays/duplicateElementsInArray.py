'''
Loop over the array

Consider each element as an index, as the elements range from 1 to len(array) we can Consider
element - 1 as an index.

Then make the element at that particular index negative, so that if we find element again 
array[element - 1] will be negative
'''
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = set()

        for e in nums:
            if nums[e - 1] < 0:
                # we've seen the element before as the index it references is negative
                dups.add(e)
            else:
                nums[e - 1] *= -1

        return list(dups)
