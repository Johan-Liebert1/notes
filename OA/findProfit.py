from typing import List


def find_profit(inventory: List[int], order: int) -> int:
    o = order
    profit = 0

    while o > 0:
        inventory = sorted(inventory)

        print(o, inventory)

        profit += inventory[-1]

        inventory[-1] -= 1

        if inventory[-1] == 0:
            inventory.pop()

        o -= 1

    return profit


print(find_profit([1000000000], 1000000000))
