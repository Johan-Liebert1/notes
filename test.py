from typing import List


class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def howSum(self, target: int, array: List[int]) -> (List):

        if target in self.memo:
            return self.memo[target]

        if target < 0:
            return None  # as the array of numbers contain only positive numbers

        if target == 0:
            return []

        for num in array:
            remainder: int = target - num
            remainder_result = self.howSum(remainder, array)

            if isinstance(remainder_result, list):
                self.memo[target] = [*remainder_result, num]
                return self.memo[target]

        self.memo[target] = None
        return None


sol = Solution()
sol2 = Solution()

print(sol.howSum(7, [2, 3]))
print(sol2.howSum(7, [5, 3, 4, 7]))
