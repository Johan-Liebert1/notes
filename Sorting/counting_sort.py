# is only able to sort positive integers and is only useful if the input array is small


def counting_sort(array: list[int]):
    if len(array) == 0:
        return []

    maxx = max(array)

    """  
        each index of this array represents an element in the actual array
        and count[i] = how many times does i appear in array? 

        1. Step 1, count the occurances of each element and store in the counts array
        2. do count[1] = count[i] + count[i - 1], 
        3. Shift the entire counts array to the right by one cell, basically count[i] = counts[i - 1].
        Now these numbers represent the position of the index in the new sorted array. 

        if counts is [1, 3, 0, 2] -> 0 apperas 1 times, 1 - 3 times, 2 - 0 times, 3 - 2 times
        adding cumulatively [1, 4, 4, 6]
        shifiting right [0, 1, 4, 4] -> i.e. 3 would be at 4th index which is similar to saying there are 4 
        elements that should appear before 3, which is true when we look at the original counts array
    """

    counts = [0] * (maxx + 1)

    for i in array:
        counts[i] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for i in range(len(counts) - 1, 0, -1):
        counts[i] = counts[i - 1]

    counts[0] = 0

    new_array = [None] * len(array)

    for i in array:
        new_array[counts[i]] = i
        counts[i] += 1

    return new_array


from helpers import get_test_case

for case in get_test_case(20, True):
    print(sorted(case[:]) == counting_sort(case))
