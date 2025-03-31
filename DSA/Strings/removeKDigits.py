"""  
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        stack = []

        """  
        if number is 3578 then we would want the lowest digits on the left and highest on the right
        so we create a graph of peaks and valleys and whereever there is a downwards slope, we remove that number
        """

        for c in num:
            while len(stack) > 0 and k > 0 and stack[-1] > c:
                stack.pop()
                k -= 1

            if len(stack) > 0 or c != "0":
                stack.append(c)

        # if all the numbers are in increasing order then we will never pop
        # if number is 1234 then we will never pop anything as 'stack[-1] > c' is never True
        # to handle that case we keep popping from the end, as if the digits are in increasing order
        # then the first (len(nums) - k) is the smallest number
        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1

        if len(stack) == 0:
            return "0"

        return "".join(stack)


print(Solution().removeKdigits("10200", 1))
