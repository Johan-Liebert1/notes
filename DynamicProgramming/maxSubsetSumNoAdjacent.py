# given an array, find the maximum sum that can be generated without summing two adjacent numbers


def function(array):
    helper = [array[0], max(array[0], array[1])]

    """  
    formula : 
    helper[i] = max(
        helper[i - 1],
        helper[i - 2] + array[i]
    )
    """

    for i in range(2, len(array)):
        helper.append(
            max(
                helper[i - 1],
                helper[i - 2] + array[i],  # two behind as numbers cannot be adjacent
            )
        )

    print(f"{helper = }")

    return helper[-1]


print(function([7, 10, 12, 7, 9, 14]))
