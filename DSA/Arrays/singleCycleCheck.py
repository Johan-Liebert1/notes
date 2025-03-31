"""  
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.

 

Example 1:

Input: nums = [2,-1,1,2,2]
Output: true
Explanation:
There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
The cycle's length is 3.
Example 2:

Input: nums = [-1,2]
Output: false
Explanation:
The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1.
By definition the sequence's length must be strictly greater than 1 to be a cycle.
Example 3:

Input: nums = [-2,1,-1,-2,-2]
Output: false
Explanation:
The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but nums[2] is negative.
Every nums[seq[j]] must be either all positive or all negative
"""

# Time = O(n) | space = O(n)
def singleCycleCheck(array) -> bool:
    visited_indices = set()
    index = 0

    while True:
        if index in visited_indices:
            break

        element = array[index]

        if index < 0:
            visited_indices.add(len(array) - abs(index))

        else:
            visited_indices.add(index)

        index += element

    return len(visited_indices) == len(array)


def singleCycleCheckBetter(array) -> bool:
    visited_indices = 0
    index = 0

    while True:
        if visited_indices > len(array):
            break

        element = array[index]

        index += element
        visited_indices += 1

    return visited_indices == len(array)


print(singleCycleCheckBetter([-1, -2, -3, -4, -5]))
