from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(len(ans)):
            ans[i] = ans[i // 2] + (i % 2)

        return ans

    def countBits2(self, n: int) -> List[int]:
        array = [0] * (n + 1)

        array[0] = 0

        if n == 0:
            return array

        array[1] = 1

        if n == 1:
            return array

        array[2] = 1

        if n == 2:
            return array

        offset = 2
        next_power_of_two = offset * 2

        for i in range(3, n + 1):
            if i == next_power_of_two:
                offset = next_power_of_two
                next_power_of_two *= 2

            array[i] = 1 + array[i - offset]

        return array
