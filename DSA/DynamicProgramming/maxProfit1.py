""" 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


from typing import List


class Solution:
    # Two pointers approach. Time = O(n) Memory = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        m = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                # don't do left += 1 here as when the right moves forward we might miss a larger profit margin
                # example = [2, 1, 2, 1, 0, 1, 2]
                left = right

            elif prices[right] - prices[left] > m:
                m = prices[right] - prices[left]

            right += 1

        return m

    # Inefficient. Time = O(2n) Memory = O(n)
    def maxProfit1(self, prices: List[int]) -> int:
        max_to_right = [0] * len(prices)
        max_to_right[-1] = 0

        for i in range(len(prices) - 2, -1, -1):
            max_to_right[i] = max(max_to_right[i + 1], prices[i + 1])

        m = 0

        for i in range(len(prices)):
            if max_to_right[i] - prices[i] > m:
                m = max_to_right[i] - prices[i]

        return m
