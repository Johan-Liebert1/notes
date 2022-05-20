from typing import Any

import random


def swap(array: list[Any], i: int, j: int):
    array[i], array[j] = array[j], array[i]


def get_test_case(x=20, no_neg=False):
    return [
        [
            random.randint(
                random.randint(-200 if not no_neg else 0, 0), random.randint(1, 200)
            )
            for _ in range(i)
        ]
        for i in range(x)
    ]
