"""
Given an unlimited supply of coins of given denominations, find the minimum number of coins required to get the desired change.

For example, consider S = { 1, 3, 5, 7 }.

If the desired change is 15, the minimum number of coins required is 3
 
(7 + 7 + 1) or (5 + 5 + 5) or (3 + 5 + 7)
 
 
If the desired change is 18, the minimum number of coins required is 4
 
(7 + 7 + 3 + 1) or (5 + 5 + 5 + 3) or (7 + 5 + 5 + 1)
"""


def min_num_of_coins_for_change(coins_available: list[int], target: int):
    result = [float("inf")] * (target + 1)

    result[0] = 0

    for coin in coins_available:
        for i in range(target + 1):
            if coin <= i:
                result[i] = min(result[i], result[i - coin] + 1)

    return result[target]


min_num_of_coins_for_change([1, 2, 4], 6)
