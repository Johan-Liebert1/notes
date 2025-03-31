import random


def shift_array(array: "list[int]", places: int):
    """Shifts the elements of array, places position to the right"""
    new_array = [None] * len(array)

    for i in range(len(array)):
        final_idx = (i + places) % len(array)

        new_array[final_idx] = array[i]

    return new_array


def binary_search(array: "list[int]", target: int, low: int, high: int) -> bool:
    while low <= high:
        middle = low + (high - low) // 2

        if array[middle] == target:
            return True

        if array[middle] < target:
            low = middle + 1

        else:
            high = middle - 1

    return False


def shifted_binary_search(array: "list[int]", target: int):
    print(f"{array=}, {target=}")

    shifted_by = 0

    for i in range(len(array) - 1):
        # assuming the array is always sorted in ascending order
        if array[i + 1] < array[i]:
            shifted_by = i + 1
            break

    low1, high1 = 0, shifted_by - 1
    low2, high2 = shifted_by, len(array) - 1

    found_left = binary_search(array, target, low1, high1)

    if found_left:
        return found_left

    found_right = binary_search(array, target, low2, high2)

    return found_right


for i in range(10):
    r = random.randint(0, 9)
    print(
        shifted_binary_search(
            shift_array([i for i in range(10)], r), random.randint(0, 10)
        ),
        end="\n\n",
    )

# max = 20

# a = [i for i in range(max)]
# print(a, end="\n")
# for i in range(15):
#     search = random.randint(0, max)

#     print(f"target = {search}", binary_search(a, search, 0, max - 1))
