from typing import List


def unique_subsets(array: List[int]) -> List[List[int]]:
    array.sort()

    superset = []

    def dfs(index: int, current_subset: List[int]):
        if index == len(array):
            superset.append([*current_subset])
            return

        # take the element at index
        current_subset.append(array[index])
        dfs(index + 1, current_subset)
        current_subset.pop()

        while index + 1 < len(array) and array[index] == array[index + 1]:
            index += 1

        # skip the element at index
        dfs(index + 1, current_subset)

    dfs(0, [])

    return superset


print(sorted(unique_subsets([1, 2, 2, 3]), key=lambda x: len(x)))
