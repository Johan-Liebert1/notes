""" Given a variety of coin denominations existing in a currency system, find the total number of ways a given amount of money can be expressed using coins in that currency system. Assume infinite supply of coins of every denomination.

Example

Input: coins = [1, 2, 3], amount = 3

Output: 3

The three ways are -

Using the coin having denomination 1 thrice
Using the coin having denomination 3 once
Using the coin having denomination 2 once and using the coin having denomination 1 once """


def ways_to_make_change(coins_availabe: list[int], target: int):
    """
    1. Initialize an array of length (target + 1). [let's say target is 10 here] [array = [1, 5, 10, 25]]
    2. array = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    every element in this array means that there are that many ways to make change for the index that the element is at

    example array[0] = 1, i.e. there is 1 way to make change for $0, i.e. to use nothing at all

    now we iterate over the array and see how many ways we can make change for the elements using a 1 dollar coin denomination
    array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    one way for all amount using only 1 dollar denomination

    formula
    array[i] = array[i] + array[i - current_coin_denomination]

    explanation
    if we're at array[6], i.e. ways to get change for $6 and current_coin_denomination is 5, then
    array[6] = array[6] + array[6 - 5 = 1]

    6 - 5 as we already have $5 and now we need 6 - 5 i.e. $1 to make $6
    """

    array = [0] * (target + 1)

    array[0] = 1

    for coin_denomination in coins_availabe:
        if coin_denomination <= target:
            for i in range(1, target + 1):
                if i >= coin_denomination:
                    array[i] += array[i - coin_denomination]

    return array[target]


print(ways_to_make_change([1, 5, 10, 25], 10))
