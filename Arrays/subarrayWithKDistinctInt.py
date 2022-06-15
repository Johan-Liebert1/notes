from typing import List


class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l, r = 0, 1
        d = {nums[l]: 1}

        count = 0

        while l <= r:
            print(f"{l = }, {r = }, {nums[l] = }, {nums[r] = }")

            if r >= len(nums):
                break

            if nums[r] not in d:
                d[nums[r]] = 1
            else:
                d[nums[r]] += 1

            if len(d.keys()) == k:
                print(d)
                count += 1
            elif len(d.keys()) > k:
                print(d)
                while True:
                    # keep removing elements from the left and only be done once the count of an element reaches 0
                    d[nums[l]] -= 1

                    if d[nums[l]] == 0:
                        del d[nums[l]]
                        l += 1
                        break

                    l += 1
                print(d)
                continue

            if r + 1 < len(nums):
                r += 1
            else:
                l += 1

        return count


a = [1, 2, 1, 2, 3]

print(Solution().subarraysWithKDistinct(a, 2))
