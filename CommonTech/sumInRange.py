"""
You have an array of integers nums and an array queries, 
where queries[i] is a pair of indices (0-based). 

Find the sum of the elements in nums from the indices at 
queries[i][0] to queries[i][1] (inclusive) for each query, 
then add all of the sums for all the queries together. 

Return that number modulo 10^9 + 7.

Example

For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
[0,2] means take nums[0], nums[1] and nums[2]

sumInRange(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10."""


def sumInRange(nums, queries):
    prefix_array = []
    total = 0

    for num in nums:
        total += num
        prefix_array.append(total)

    final_total = 0

    for indices in queries:
        final_total += prefix_array[indices[1]] - prefix_array[indices[0]]

    return final_total % int(10e8 + 7)
