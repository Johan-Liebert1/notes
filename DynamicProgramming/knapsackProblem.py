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

Two choices
1. values[i - 1][j] = current item has a weight larger than the knapsack OR putting in the current item has no increase in profit

2.

values[i][j] = max (
    values[i - 1][j],
    values[i - 1][j - w] + v    # w = weight of current item, v = value of current item
)

values[i - 1][j - w] + v = current item can fit in the knapsack. So we check if we removed a weight equivalent to the current item's weight from the previous row, will that sum be higher than just not adding the current item
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

    # for v in values:
    # print(v)

    return values[-1][-1]


def knapsack_recursion(items: list[list[int]], knapsack_size: int):
    def recurse(
        item_index: int, current_knapsack_size: int, max_profit_yet: list[int]
    ) -> int:
        if item_index > len(items) - 1 or current_knapsack_size == 0:
            return 0

        if item_index == len(items) - 1:
            return (
                max_profit_yet[0] + items[-1][0]
                if items[-1][1] <= current_knapsack_size
                else max_profit_yet[0] + 0
            )

        max_profit = 0

        # do not iterate, since this is a recursive solution, we only process one item at a time
        # for item in items[item_index:]:
        value, weight = items[item_index]

        if weight > current_knapsack_size:
            max_profit = recurse(item_index + 1, current_knapsack_size, max_profit_yet)

        else:
            max_profit = max(
                value
                + recurse(
                    item_index + 1, current_knapsack_size - weight, max_profit_yet
                ),
                recurse(item_index + 1, current_knapsack_size, max_profit_yet),
            )

        max_profit_yet[0] = max(max_profit, max_profit_yet[0])

        return max_profit

    a = [0]
    recurse(0, knapsack_size, a)

    return a[0]


memo = knapsack_problem(
    [
        [4, 3],
        [6, 7],
        [5, 6],
        [1, 2],
    ],
    5,
)

recurse = knapsack_recursion(
    [
        [4, 3],
        [6, 7],
        [5, 6],
        [1, 2],
    ],
    5,
)

print(f"{memo = } | {recurse = }")
