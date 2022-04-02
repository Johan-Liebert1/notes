from typing import List
import sys

# O(n! * n^2) time | O(n! * n) space
def permutations(array: "list") -> "list[list]":
    permutations = []
    perm_helper(array, [], permutations)

    return permutations


def perm_helper(
    array: "list", current_permutation: "list", all_permutations: "list[list]"
):
    if len(array) == 0 and len(current_permutation) > 0:
        all_permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            # remove the current number from the array
            # as that number will be shuffled around in the array to create permuataions
            new_array = array[:i] + array[i + 1 :]

            new_permuataion = current_permutation + [array[i]]

            perm_helper(new_array, new_permuataion, all_permutations)


# O(n! * n) time | O(n! * n) space
def permuatations_better(array) -> "list[list]":
    permuatations = []
    helper_perm_better(0, array, permuatations, 0)

    return permuatations


def swap(list: List, i: int, j: int):
    list[i], list[j] = list[j], list[i]


def helper_perm_better(
    index: int, array: "list", all_permutations: "list[list[int]]", depth: int
):

    print(f"{depth = } \n\t{index = } \n\t{array = } \n\t{all_permutations} \n\n")

    if index == len(array) - 1:
        all_permutations.append(array[:])

    else:
        for j in range(index, len(array)):
            swap(array, index, j)
            helper_perm_better(index + 1, array, all_permutations, depth + 1)
            swap(array, index, j)


print(permuatations_better([i for i in range(int(sys.argv[1]))]))
