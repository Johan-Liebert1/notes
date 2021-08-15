'''
function returns a bool indicating whether it is possible to 
get the target sum from the numbers in the array. Numbers can
be used multiple times.
'''


def targetSum(target, array, memo={}):
    print(memo)
    if target in memo:
        return memo[target]

    if target < 0:
        return False

    if target == 0:
        return True

    for i in array:
        if targetSum(target - i, array,  memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


print(targetSum(7, [2, 3]))
print(targetSum(7, [5, 3, 4, 7]))

print(targetSum(300, [7, 14]))
