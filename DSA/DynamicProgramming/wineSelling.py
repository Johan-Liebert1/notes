"""  
Given n wines in a row, with integers denoting the cost of each wine respectively. 
Each year you can sell the first or the last wine in the row.
Let the initial profits from the wines be P1, P2, P3…Pn.
In the Yth year, the profit from the ith wine will be Y*P[i].
The goal is to calculate the maximum profit that can be earned by selling all the wines.
"""

"""  
Input: Price of wines: 2 4 6 2 5
Output: beg end end beg beg 
         64

The initial thought would be to go greedy, that is, check both the ends and sell the cheaper wine every time. If we do it greedy way,

price = 1*2 =  2, remaining wines = [ 4, 6, 2, 5 ], Profit = 2
price = 2*4 =  8, remaining wines = [ 6, 2, 5 ], Profit = 10
price = 3*5 = 15, remaining wines = [ 6, 2 ], Profit = 25
price = 4*2 =  8, remaining wines = [ 6 ], Profit = 33
price = 5*6 = 30, remaining wines = [ ], Profit = 63

This is wrong since the output is 64

Correct :
price = 1*2 =  2, remaining wines = [ 4, 6, 2, 5 ], Profit = 2
price = 2*5 = 10, remaining wines = [ 4, 6, 2 ], Profit = 12
price = 3*2 =  6, remaining wines = [ 4, 6], Profit = 18
price = 4*4 = 16, remaining wines = [ 6 ], Profit = 34
price = 5*6 = 30, remaining wines = [ ], Profit = 64
"""

# Time O(2^n)
def max_profit_backtracking(wine: list[int], start: int, end: int, y: int) -> int:
    if start == end:
        # only one bottle left to sell so just return that
        return wine[start] * y

    # selling the left wine bottle
    left = (wine[start] * y) + max_profit_backtracking(wine, start + 1, end, y)

    # selling the right wine bottle
    right = (wine[end] * y) + max_profit_backtracking(wine, start, end - 1, y)

    return max(left, right)


# Time O(N * N)
def max_profit_dp(
    wine: list[int], start: int, end: int, y: int, dp: list[list[int]]
) -> int:
    if dp[start][end] != -1:
        # dp[start][end] = what's the max profit for array[start: end]
        return dp[start][end]

    if start == end:
        # only one bottle left to sell so just return that
        return wine[start] * y

    # selling the left wine bottle
    left = (wine[start] * y) + max_profit_dp(wine, start + 1, end, y)

    # selling the right wine bottle
    right = (wine[end] * y) + max_profit_dp(wine, start, end - 1, y)

    dp[start][end] = max(left, right)

    return dp[start][end]
