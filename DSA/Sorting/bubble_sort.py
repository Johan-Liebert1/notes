from helpers import get_test_case, swap


def bubble_sort(array: "list[int]"):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                swap(array, i, j)


a = get_test_case()

print(a)

bubble_sort(a)

print(a, a == sorted(a))
