def swap(array: "list", i: int, j: int):
    array[i], array[j] = array[j], array[i]


def partition_array(array: "list[int]", left: int, right: int):
    pivot = array[left]
    left += 1

    while left <= right:
        while array[left] <= pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left < right:
            swap(array, left, right)

    swap(array, 0, right)


# fmt:off
array = [3,6,4,1,-1, 5, 6, 0, -2, 2, -5]

# fmt:on
partition_array(array, 0, len(array) - 1)

print(array)
