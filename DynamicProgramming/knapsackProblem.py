"""
Input = (
    Array [ [price_of_item, weight_of_item],... ],
    Integer bag_size
)

"""

_ = """ 

        0   1   2   3   4   5 -> knapsack size
[]      0   0   0   0   0   0 
[v1,w1] 
[v2,w2]
[v3,w3]
[v4,w4]

|
v
[item_value, item_weight]

values[i][j] = max (
    values[i - 1][j],
    values[i - 1][j - w] + v # w = weight of current item, v = value of current item
)

1. values[i - 1][j] = current item as a weight larger than the knapsack OR putting in the current item as no increase in profit

2. values[i - 1][j - w] + v = current item can fit in the knapsack. So we check if we removed a weight equivalent to the current item's weight from the previous row, will that sum be higher than just not adding the current item
"""


def knapsack_problem(items: "list[list[int]]", knapsack_size: int):
    """
    items = [[item_value, item_weight],...]
    """

    values = [[0 for _ in range(knapsack_size + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(values)):
        current_item_value, current_item_weight = items[i - 1]

        for col in range(len(values[0])):
            # here col is the knapsack_size we're checking for
            if current_item_weight > col:
                values[i][col] = values[i - 1][col]

            else:
                values[i][col] = max(
                    values[i - 1][col],
                    values[i - 1][col - current_item_weight] + current_item_value,
                )

    for v in values:
        print(v)


knapsack_problem([[1, 2], [4, 3], [5, 6], [6, 7]], 10)
