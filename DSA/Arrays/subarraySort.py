"""  
Given a paritally sorted array, find the smallest subarray that must be sorted for the
entire array to be sorted

ex:
input = [1, 3, 6, 0, 4, 9]
subarray to be sorted = [1, 3, 6, 0, 4]
return the indicies of the elements
"""


def subarray_sort(array: list[int]) -> list[int]:
    result = []

    lowest_unsorted_element_index, highest_unsorted_element_index = float("inf"), float(
        "-inf"
    )

    if array[0] > array[1]:
        lowest_unsorted_element_index = 0

    # find the indicies of the first and last unsorted elements
    # this might not be the subarray that we want to sort
    for i in range(1, len(array) - 1):
        if array[i] < array[i - 1] or array[i] > array[i + 1]:
            lowest_unsorted_element_index = min(lowest_unsorted_element_index, i)
            highest_unsorted_element_index = max(highest_unsorted_element_index, i)

    min_unsorted_element, max_unsorted_element = float("inf"), float("-inf")

    # find the smallest and largest unsorted element
    for i in range(lowest_unsorted_element_index, highest_unsorted_element_index + 1):
        if array[i] < min_unsorted_element:
            min_unsorted_element = array[i]
            lowest_unsorted_element_index = i

        if array[i] > max_unsorted_element:
            max_unsorted_element = array[i]
            highest_unsorted_element_index = i

    # find the final position in the array for the smallest and largest unsorted element
    for i in range(1, len(array) - 1):
        if (
            array[i - 1] < min_unsorted_element <= array[i]
            and i != lowest_unsorted_element_index
        ):
            result.append(i)
            break

    if len(result) == 0:
        result.append(0)

    for i in range(1, len(array) - 1):
        if (
            array[i - 1] < max_unsorted_element <= array[i]
            and i != highest_unsorted_element_index
        ):
            # i - 1 as this condition is hit after we move past the insertion index
            result.append(i - 1)
            break

    if len(result) == 1:
        result.append(len(array) - 1)

    return result


print(
    subarray_sort(
        [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        # [1, 3, 6, 0, 4, 9]
    )
)
