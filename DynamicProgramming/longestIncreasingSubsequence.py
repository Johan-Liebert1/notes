# Dynamic Programming Sol (medium difficulty)


# Time: O(n ^ 2) | Space: O(n)
def longest_increasing_subsequence_dp(array: list[int]) -> list[int]:
    sequences: list[None | int] = [None] * len(array)

    """
    lengths[i] = length of longest increasing subsequence that ends with array[i]   
    """
    lengths = [1] * len(array)

    max_len_idx = 0

    for i in range(len(array)):
        current_num = array[i]

        for j in range(i):
            other_num = array[j]

            if other_num < current_num and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j

        # as we need to know which index to start building our sequence from
        if lengths[i] >= lengths[max_len_idx]:
            max_len_idx = i

    return build_sequence(array, sequences, max_len_idx)

def lis(array: list[int]) -> list[int]:
    # lis_cache[i] = length of longest increasing subsequence that starts with lis_cache[i]   
    lis_cache = [1] * len(array)

    max_len_idx = 0

    sequences: list[None | int] = [None] * len(array)

    for i in range(len(array) - 1, -1, -1):
        for j in range(i + 1, len(array)):
            if array[i] < array[j] and 1 + lis_cache[j] > lis_cache[i]:
                lis_cache[i] = 1 + lis_cache[j]
                sequences[i] = j

        if lis_cache[i] > lis_cache[max_len_idx]:
            max_len_idx = i

    return build_sequence(array, sequences, max_len_idx)

def binary_search(
    indicies: list[None | int],
    start: int,
    end: int,
    array: list[int],
    current_number: int,
):
    if start > end:
        return start

    middle = (start + end) // 2

    if array[indicies[middle]] < current_number:
        start = middle + 1
    else:
        end = middle - 1

    return binary_search(indicies, start, end, array, current_number)


# Time: O(n * log(n)) | Space: O(n)
def longest_increasing_subsequence_clever(array: list[int]) -> list[int]:
    sequences: list[None | int] = [None] * len(array)

    """  
    indicies[i] = which index does longest increasing subsequence of length i ends at if it exists, else None
    The samllest number that can end an increasing subsequence of length i
    """
    indicies: list[None | int] = [None] * (len(array) + 1)

    current_longest_subseq_len = 0

    for (i, num) in enumerate(array):
        new_length = binary_search(indicies, 1, current_longest_subseq_len, array, num)

        sequences[i] = indicies[new_length - 1]
        indicies[new_length] = i

        current_longest_subseq_len = max(current_longest_subseq_len, new_length)

    return build_sequence(array, sequences, indicies[current_longest_subseq_len])


def build_sequence(
    array: list[int], sequences: list[None | int], max_len_idx: int | None
) -> list[int]:
    sequence = []

    current_idx = max_len_idx

    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]

    return sequence[::-1]


print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
