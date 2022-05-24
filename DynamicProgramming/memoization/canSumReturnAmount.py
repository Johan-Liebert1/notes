"""  
Given an array A, and target T, return how many subsets of the array can sum up to the target
"""

# recursive approach
# Time = O(2 ^ n) | Space O(n)
def can_sum_return_amount_recursive(array: list[int], target: int) -> int:
    count = 0

    def recurse(current_index: int, current_target: int):
        nonlocal count

        local_count = 0

        if current_target == 0:
            # reached a target of 0, ie. were able to find something that summed up to the target
            count += 1
            return

        # two choices for each element, whether to include it or not in the final sum
        if current_index == len(array) - 1:
            count += 1 if array[-1] == current_target else 0
            return

        if current_target < array[current_index]:
            # skip this element as it's larger than the target sum
            recurse(current_index + 1, current_target)

        else:
            # skip the current element and check if rest of the elements can sum up to the target sum
            recurse(current_index + 1, current_target)
            # don't skip the current element and check if rest of the elements can sum up to
            # the new target (current_target - array[current_index])
            recurse(
                current_index + 1,
                current_target
                - (
                    array[current_index]
                    if array[current_index] > 0
                    else -array[current_index]
                ),
            )

        return local_count

    recurse(0, target)

    return count


# Time O(len(array) * target) | Space = time
def can_sum_return_amount_iterative(array: list[int], target: int) -> int:
    """
    same idea as knapsack, put sum (from 0 - target) on one axis
    and array indicies on the other
    """

    values = [
        # first column is 1 as there is only 1 way to get a sum of 0, which is to not use any element
        [1 if col == 0 else 0 for col in range(target + 1)]
        for _ in range(len(array) + 1)
    ]

    for row in range(1, len(values)):
        array_value = array[row - 1]
        for current_target in range(1, len(values[0])):
            # if the target smaller than the array element, then just skip
            if current_target < array_value:
                values[row][current_target] = values[row - 1][current_target]

            # else subtract the current array element from the current_target
            # go one row up, as we used up an array element by subtracting it from current_target, so now
            # current_target = current_target - array[row - 1]
            # go array[row - 1] columns to the left and check how many ways we could sum that up and add that
            # value to values[row][current_target]
            else:
                print(
                    f"{current_target - array_value = } {array_value = } {current_target = } {row = }"
                )

                values[row][current_target] = (
                    values[row - 1][current_target]
                    + values[row - 1][
                        current_target
                        - (
                            # if array_value is negative, we'll need to add it to the current target
                            array_value
                            if array_value > 0
                            else -array_value
                        )
                    ]
                )

    return values[-1][-1]


array = [1, 2, 4, -1, 1]
target = 3

print(
    f"{can_sum_return_amount_recursive(array, target) = } | {can_sum_return_amount_iterative(array, target)}"
)
