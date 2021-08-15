'''
Given an array of integers nums and an integer k, 
determine whether there are two distinct indices i and j 
in the array where nums[i] = nums[j] and the absolute 
difference between i and j is less than or equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
containsCloseNums(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.'''


def containsCloseNums(nums, k):
    d = {}

    for index, value in enumerate(nums):
        if value not in d:
            d[value] = [index]

        else:
            d[value].append(index)


    for key, value in d.items():

        if len(value) > 1:
            for i in range(len(value) - 1):
                if abs(value[i] - value[i+1]) <= k:
                    return True
     

    return False, d



nums = [1, 0, 1, 1]
k = 1

print(containsCloseNums(nums, k))