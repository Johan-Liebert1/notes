"""
Also Called Quickselect

Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

Example

For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
kthLargestElement(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
kthLargestElement(nums, k) = 99."""

nums = [3, 6, 4, 1, -1, 5, 6, 0, -2, 2, -5]


def kth_largest_naive(array, k):
    new_arr = sorted(array)
    return new_arr[len(new_arr) - k]


def swap(array: "list", i: int, j: int):
    array[i], array[j] = array[j], array[i]


def quickselect(array: "list[int]", k: int, left: int, right: int):
    while True:
        if left > right:
            break

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

        swap(array, pivot_index, high)

        if high == k:
            return array[high]

        elif high < k:
            left = high + 1

        else:
            right = high - 1


def kth_largest_clever(array: "list[int]", k: int):
    # impement quick sort partition technique
    return quickselect(array, len(array) - k, 0, len(array) - 1)


print(sorted(nums), kth_largest_clever(nums, 5))
