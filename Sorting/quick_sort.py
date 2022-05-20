from helpers import get_test_case, swap


def partition(array: list[int], left: int, right: int) -> int:
    pivot_index = left
    low = left + 1
    high = right

    while low <= high:
        if array[low] > array[pivot_index] and array[high] < array[pivot_index]:
            swap(array, low, high)

        if array[low] <= array[pivot_index]:
            low += 1

        if array[high] >= array[pivot_index]:
            high -= 1

    swap(array, high, pivot_index)

    return high


def quick_sort(array: list[int], left: int, right: int):
    if left > right or left < 0 or right > len(array) - 1:
        return

    final_pos = partition(array, left, right)

    quick_sort(array, left, final_pos - 1)
    quick_sort(array, final_pos + 1, right)


cases = get_test_case()

for case in cases:
    pysort = sorted(case[:])

    quick_sort(case, 0, len(case) - 1)

    print(pysort == case, case)
