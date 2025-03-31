"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""


# slower DP
def coinChangeDP(coins: list[int], amount: int) -> int:
    amounts = [-1] * (amount + 1)
    amounts[0] = 0

    coins.sort()

    coins_set = set(coins)

    for i in range(1, amount + 1):

        if i in coins_set:
            amounts[i] = 1

        else:
            min_yet = float("inf")

            for c in coins:
                if c > i:
                    continue

                min_yet = min(min_yet, 1 + amounts[i - c])

            amounts[i] = min_yet

    for (i, e) in enumerate(amounts):
        if e == float("inf"):
            continue
        print(f"Value: {i}, Coins: {e}")

    return -1 if amounts[-1] == float("inf") else amounts[-1]


def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    cur = 1 << amount  # Get the number as if it was binary
    step = 1

    while True:
        prev = cur
        for coin in coins:
            cur = cur | (prev >> coin)

        if cur == prev:  # If, after a round we have no deductions
            return -1
        if cur & 1:
            return step

        step += 1


print(coinChange([1, 2, 3, 5], 11))
