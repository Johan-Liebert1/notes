'''
function returns an array containing the numbers that add up  
to the target sum from the numbers in the array. Numbers can
be used multiple times.

If there are multiple combinations, return any one of them
'''

from typing import List


def howSum(target: int, array: List[int], memo=None) -> (List):
    if not isinstance(memo, dict):
        '''
        The reason is simple: the function keeps using the same object, in each call. 
        The modifications we make are “sticky”.

        Default parameter values are always evaluated when, and only when, 
        the “def” statement they belong to is executed
        '''
        memo = {}

    if target in memo:
        return memo[target]

    if target < 0:
        return None  # as the array of numbers contain only positive numbers

    if target == 0:
        return []

    for num in array:
        remainder: int = target - num
        remainder_result = howSum(remainder, array, memo)

        if isinstance(remainder_result, list):
            memo[target] = [*remainder_result, num]
            return memo[target]

    memo[target] = None
    return None


first = howSum(7, [2, 3])
print(first)


second = howSum(7, [5, 3, 4, 7])
print(second)

print(howSum(7, [2, 4]))
print(howSum(8, [1]))
print(howSum(300, [7, 14]))
