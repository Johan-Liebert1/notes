"""  
Given an array of integers, find the maximum sum that can be generated if we only
consider an increasing subsequence of the array. 
"""


def max_sum_increasing_subsequence(array: "list[int]"):
    sum_until_index = [float("-inf")] * len(array)
    sequences = [None] * len(array)  # to store what numbers gave us the max sum

    max_sum_index = -1

    for i, current_element in enumerate(array):
        sum_until_index[i] = current_element

        for j in range(i):
            if array[j] < current_element:
                if sum_until_index[i] < sum_until_index[j] + current_element:
                    sum_until_index[i] = sum_until_index[j] + current_element
                    sequences[i] = j

        max_sum_index = (
            i if sum_until_index[i] > sum_until_index[max_sum_index] else max_sum_index
        )

    i = max_sum_index
    elements = []

    while i is not None:
        elements.append(array[i])
        i = sequences[i]

    print(sum_until_index, elements)


max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7])
