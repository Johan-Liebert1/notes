from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        superset = [[]]

        for num in nums:
            length = len(superset)
            for i in range(length):
                superset.append([*superset[i], num])

        return superset

    def subsets_recursive(self, nums: List[int]) -> List[List[int]]:
        superset = []

        def dfs(index: int, current_subset: List[int]):
            if index == len(nums):
                superset.append([*current_subset])
                return

            # take the element at index
            current_subset.append(nums[index])
            dfs(index + 1, current_subset)

            # pop the element as we don't want it for the next call
            current_subset.pop()

            # skip the element at index
            dfs(index + 1, current_subset)

        dfs(0, [])

        return superset


s = Solution()

a = [1, 2, 3]

print("iterative", sorted(s.subsets(a), key=lambda x: len(x)))
print("recursive", sorted(s.subsets_recursive(a), key=lambda x: len(x)))
