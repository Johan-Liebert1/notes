from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        superset = [[]]

        for num in nums:
            length = len(superset)
            for i in range(length):
                superset.append([*superset[i], num])

        return superset


print(Solution().subsets([1, 2, 3]))
