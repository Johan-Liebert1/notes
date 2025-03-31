from typing import List


class Solution:
    def is_self_dividing(self, num: int) -> bool:
        actual_num = num

        while num > 0:
            tmp = num % 10

            if tmp == 0 or actual_num % tmp != 0:
                return False

            num //= 10

        return True

    def cheat(self, left, right):
        li, ri = -1, -1

        for i, e in enumerate(array):
            if e >= left and li == -1:
                li = i

            if e <= right:
                ri = i

        return array[li : ri + 1]

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # return self.cheat(left, right)

        a = []

        for i in range(left, right + 1):
            if self.is_self_dividing(i):
                a.append(i)

        return a


print(Solution().selfDividingNumbers(1, 10000))
