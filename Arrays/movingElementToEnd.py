from typing import List


def movingElementToEnd(array: List[int], element: int):
    front, back = 0, len(array) - 1

    if array[back] == element:
        back -= 1

    while front <= back:
        print(array, front, back)

        if array[front] == element:
            array[front], array[back] = array[back], array[front]

            front += 1
            back -= 1

        else:
            front += 1

    return array


def move_zeros(array):
    non_zero, zero = [], []

    for i in array:
        if i == 0:
            zero.append(i)

        else:
            non_zero.append(i)

    array = non_zero + zero

    print(array)


# print(movingElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 1))
move_zeros([0, 1, 0, 3, 12])
