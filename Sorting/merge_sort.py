def merge(
    main_array: list[int],
    start_index: int,
    middle_index: int,
    end_index: int,
    auxiliary_array: list[int],
):
    i = start_index
    j = middle_index + 1
    k = start_index

    # first subarray starts at start_index and ends at middle_index
    # second subarray starts at middle_index + 1 and ends at end_index

    while i <= middle_index and j <= end_index:
        if auxiliary_array[i] <= auxiliary_array[j]:
            main_array[k] = auxiliary_array[i]
            i += 1

        else:
            main_array[k] = auxiliary_array[j]

        k += 1

    while i <= middle_index:
        main_array[k] = auxiliary_array[i]
        i += 1
        k += 1

    while j <= end_index:
        main_array[k] = auxiliary_array[j]
        j += 1
        k += 1


def merge_sort_helper(
    main_array: list[int], start_index: int, end_index: int, auxiliary_array: list[int]
):
    if start_index == end_index:
        # one element
        return

    middle_index = (start_index + end_index) // 2

    merge_sort_helper(auxiliary_array, start_index, middle_index, main_array)
    merge_sort_helper(auxiliary_array, middle_index + 1, end_index, main_array)

    merge(main_array, start_index, middle_index, end_index, auxiliary_array)


def merge_sort(array: list[int]):
    if len(array) <= 1:
        return array

    auxiliary_array = array[:]

    merge_sort_helper(array, 0, len(array) - 1, auxiliary_array)

    return array
