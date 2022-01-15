"""  
can think of this as two number sum twice. 
"""


def add_quadruplet_to_results(
    current_pair: list[int], results: list[list[int]], pairs: list[list[int]]
):
    for pair in pairs:
        results.append([*current_pair, *pair])


# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space
def four_number_sum(array: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []

    hash_table: dict[int, list[list[int]]] = {}

    for (i, element) in enumerate(array):
        # iterate to the right
        for j in range(i + 1, len(array)):
            to_find = target - (element + array[j])
            if to_find in hash_table:
                add_quadruplet_to_results(
                    [element, array[j]], result, hash_table[to_find]
                )

        for j in range(i - 1, -1, -1):
            to_add = element + array[j]

            if to_add not in hash_table:
                hash_table[to_add] = [[element, array[j]]]
            else:
                hash_table[to_add].append([element, array[j]])

    print(hash_table)

    return result


print(four_number_sum([7, 6, 4, -1, 1, 2], 16))
