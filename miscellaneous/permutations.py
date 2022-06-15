from typing import List, Union
import sys


# O(n! * n^2) time | O(n! * n) space
def permutations(array: List) -> List[List]:
    permutations_array = []
    perm_helper(array, [], permutations_array)
    return permutations_array


def perm_helper(array: List, current_permutation: List,
                all_permutations: List[List]):
    if len(array) == 0 and len(current_permutation) > 0:
        all_permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            # remove the current number from the array
            # as that number will be shuffled around in the array to create permuataions
            new_array = array[:i] + array[i + 1:]

            new_permuataion = current_permutation + [array[i]]

            perm_helper(new_array, new_permuataion, all_permutations)


# O(n! * n) time | O(n! * n) space
def permuatations_better(s: Union[str, List]):
    permutations_array = []

    def helper(s: list[str], index: int):
        # whatever the index is, is fixed
        # then we'll swap every other element with s[index + 1]

        if index == len(s) - 1:
            permutations_array.append([*s])
            return

        for i in range(index, len(s)):
            s[i], s[index] = s[index], s[i]

            helper(s, index + 1)

            s[i], s[index] = s[index], s[i]

    helper(list(s), 0)

    return permutations_array


# fmt:off
print(permuatations_better(list(range(int(sys.argv[1])))))
