from typing import List


class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        # basically find the longest subarray that has sum = sum(nums) - x
        # this is because if the subarray is the longest that has the above sum
        # then we'd use lowest edge number

        # { prefix_sum => index }
        prefix_sums = {0: 0, nums[0]: 0}

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            prefix_sums[nums[i]] = i

        target = nums[-1]

        target -= x

        print(nums, target, prefix_sums)

        min_max = [0, -100]

        for i, e in enumerate(nums):
            if e - target in prefix_sums:
                if i - prefix_sums[e -
                                   target] + 1 > min_max[1] - min_max[0] + 1:
                    min_max = [prefix_sums[e - target] + 1, i]
        print(min_max)
        l = min_max[1] - min_max[0]

        return len(nums) - (l + 1) if sum(min_max) >= 0 else -1

    # Slow af. TLE
    def minOperationsTLE(self, nums: List[int], x: int) -> int:
        cache = {}

        def recurse(left, right, target, depth):
            if (left, right, depth) in cache:
                print((left, right, depth), "cache hit")
                return cache[(left, right, depth)]

            if right < 0 or left >= len(nums) or target < 0:
                return float("inf")

            if target == 0:
                return depth

            l, r = float("inf"), float("inf")

            if nums[left] <= target:
                l = recurse(left + 1, right, target - nums[left], depth + 1)

            if nums[right] <= target:
                r = recurse(left, right - 1, target - nums[right], depth + 1)

            cache[(left, right, depth)] = min(l, r)

            return cache[(left, right, depth)]

        return recurse(0, len(nums) - 1, x, 0)


print(Solution().minOperations([3, 2, 20, 1, 1, 3], 10))
