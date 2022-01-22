"""  
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The rst number in the output array should be the rst number in the range while the second number should be the last number in the range. A range of numbers is dened as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.

Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] Sample output: [0, 7]
as 0,1,2,3,4,5,6,7 appear in the array
"""


def largest_range(array: list[int]) -> list[int]:
    hash_table = {k: True for k in array}

    # True = number is still good to explore as we don't want to iterate on the numbers in a single range multiple times

    low, high = float("inf"), float("-inf")

    for element in array:
        current_low, current_high = float("inf"), float("-inf")

        if hash_table[element] == True:
            # this element hasn't been included in any range
            hash_table[element] = False

            # iterate backwards
            i = 1

            while (element - i) in hash_table:
                current_low = min(current_low, element - i)
                hash_table[element - i] = False

                i += 1

            # iterate forwards
            i = 1

            while (element + i) in hash_table:
                current_high = max(current_high, element + i)
                hash_table[element + i] = False

                i += 1

        if current_low != float("inf") and current_high != float("-inf"):
            if current_high - current_low > high - low:
                low = min(low, current_low)
                high = max(high, current_high)

    return [low, high]


print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
