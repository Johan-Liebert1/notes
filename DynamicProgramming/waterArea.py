"""  
Given an array A where each element in A represents a piller height. Find the area of the space in 
between the pillers


Example 
A = [10, 0, 10]
area = 10 (considering pillers of unit length) as water can only be trapped in between the two pillers of 
height 10

A = [10, 10]
area = 0
as there's no space between the pillers for water to get trapped
"""


def water_area(array: "list[int]"):
    max_piller_height_right = [0] * len(array)
    max_piller_height_left = [0] * len(array)

    for i in range(1, len(array)):
        max_piller_height_left[i] = max(array[i - 1], max_piller_height_left[i - 1])

    for i in range(len(array) - 2, -1, -1):
        max_piller_height_right[i] = max(array[i + 1], max_piller_height_right[i + 1])

    total_area = 0

    for i, height in enumerate(array):
        min_height = min(max_piller_height_left[i], max_piller_height_right[i])

        water = 0

        if height < min_height:
            water = min_height - height

        # print(f"Index = {i}, {min_height=}, {water=}, {min_height-height=}")

        total_area += water

    return total_area


water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
