"""  
Given an array A, and target T, return how many subsets of the array can sum up to the target
Not allowed to use same element twice
"""

# recursive approach
# Time = O(2 ^ n) | Space O(n)
def can_sum_return_amount_recursive(array: list[int], target: int) -> int:
    count = 0

    def recurse(current_index: int, current_target: int, depth: int = 0):
        nonlocal count

        local_count = 0

        if current_target == 0:
            # reached a target of 0, ie. were able to find something that summed up to the target
            count += 1
            return

        # two choices for each element, whether to include it or not in the final sum
        if current_index == len(array) - 1:
            count += 1 if current_target % array[-1] == 0 else 0
            return

        if current_target < array[current_index]:
            # skip this element as it's larger than the target sum
            recurse(current_index + 1, current_target, depth + 1)

        else:
            # skip the current element and check if rest of the elements can sum up to the target sum
            recurse(current_index + 1, current_target, depth + 1)
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
                depth + 1,
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


array = [5]
target = 10

print(
    f"{can_sum_return_amount_recursive(array, target) = } | {can_sum_return_amount_iterative(array, target) = }"
)


"""  
Given an array A, and target T, return how many subsets of the array can sum up to the target
Allowed to use same element twice
"""


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def recurse(index: int, target: int):
            if (index, target) in cache:
                return cache[(index, target)]

            if target == 0:
                return 1

            if index == len(coins) - 1:
                return 1 if target % coins[-1] == 0 else 0

            if target < 0:
                return 0

            cache[(index, target)] = recurse(index, target - coins[index]) + recurse(
                index + 1, target
            )

            return cache[(index, target)]

        return recurse(0, amount)


print(Solution().change(4, [1, 2]))


"""  
Maintain a prefix sum at every index in the array like, { prefix_sum: number_of_times_this_sum_occurs }

keep track of the cumulative sum until now in a variable s

at every point in the iteration, check if (s - k) is in prefix_sums dict. We want (s - k) as, if s (the cumulative sum)
is equal to 18 and k = 3, then if we find a prefix sum that is 15 (18 - 3) then removing that prefix will 
give us the sum of 3 which is what we want

We add a base case of 0 as the empty subarray having sum of 0. Because, if s = 3 and k = 3, then 3 - 3 = 0, but we might
not have 0 in out prefix sums and we will end up not counting this subarray
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        prefix_sums = {0: 1}
        s = 0
        c = 0

        for i in nums:
            s += i

            if s - k in prefix_sums:
                c += prefix_sums[s - k]

            if s in prefix_sums:
                prefix_sums[s] += 1
            else:
                prefix_sums[s] = 1

        return c
