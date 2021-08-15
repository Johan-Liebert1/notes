'''
function returns an array containing the numbers that add up  
to the target sum from the numbers in the array. Numbers can
be used multiple times.

If there are multiple combinations, return the one with least numbers used
'''


def bestSumRecursion(target, array, memo=None):

    if not isinstance(memo, dict):
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    current_shortest = None

    for num in array:
        rem = target - num

        returned = bestSumRecursion(rem, array, memo)

        if isinstance(returned, list):
            arr = [*returned, num]

            if not current_shortest or len(arr) < len(current_shortest):
                current_shortest = arr

    memo[target] = current_shortest
    return current_shortest


print(bestSumRecursion(7, [2, 5, 1, 3, 4]))
print(bestSumRecursion(100, [2, 5, 1, 25]))
