from typing import List


def three_largest_numbers(arr: List[int]) -> List[int]:
    new_arr = ['_'] * 3

    for element in arr:
        if new_arr[-1] == '_':
            new_arr[-1] = element

        elif element > new_arr[-1]:
            new_arr[-3] = new_arr[-2]
            new_arr[-2] = new_arr[-1]
            new_arr[-1] = element

        elif new_arr[-2] == '_':
            new_arr[-2] = element

        elif element > new_arr[-2]:
            new_arr[-3] = new_arr[-2]
            new_arr[-2] = element

        elif new_arr[-3] == '_' or new_arr[-3] < element:
            new_arr[-3] = element

    return new_arr


print(three_largest_numbers([11, 65, 193, 36, 209, 664, 32]))
