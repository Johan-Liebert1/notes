def productSum(arr, depth=1):
    total_sum = 0

    for i in arr:
        if (isinstance(i, list)):
            total_sum += productSum(i, depth + 1)

        else:
            total_sum += i

    return total_sum * depth


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
