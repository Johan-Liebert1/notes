"""  
given some arbitrary digits of PI and and array containing some numbers, find the minimum
number of spaces that when added at concise places in the original number, results in all the resulting
space separated numbers to be a part of the numbers given in the array

ex

number = 3141592
array = [3141, 5, 31, 2, 4159, 5, 9, 42]

answer = 2 spaces

31 4159 2

"""


def get_min_spaces_for_number(
    digits: str, start: int, end: int, fav_numbers: set[int], cache: dict[str, int]
):
    """
    split the number into prefix and suffix -> 3141592 => 3 | 141592
    then if the prefix is in fav_numbers, recursively call get_min_spaces_for_number on the suffix
    """

    if start >= end:
        print("end - start <= 0")
        return -1

    number = digits[start:end]

    if number in cache:
        return cache[number]

    if len(number) == 1 and number in fav_numbers:
        return 0

    min_spaces = float("inf")

    for i in range(start, end):
        prefix = digits[start:i]

        if prefix in fav_numbers:
            min_spaces_for_suffix = get_min_spaces_for_number(
                digits, i, end, fav_numbers, cache
            )

            print(f"{prefix = }, {min_spaces_for_suffix = }, {digits[i: end] = }")

            min_spaces = min(min_spaces, min_spaces_for_suffix + 1)

    cache[number] = min_spaces

    return min_spaces


def get_min_spaces(digits: str, fav_numbers: list[str]) -> int:
    fav_numbers_set = set([str(i) for i in fav_numbers])
    cache: dict[str, int] = {}

    min_spaces = get_min_spaces_for_number(
        digits, 0, len(digits), fav_numbers_set, cache
    )

    return min_spaces


print(get_min_spaces("3141592", [3141, 5, 31, 2, 4159, 5, 9, 42]))
