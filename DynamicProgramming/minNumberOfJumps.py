"""  
Given an array, find the minimum number of jumps required to reach the end of the array
from the beginning of the array.

At any index i in the array, the number of steps that you can take forward is the value at
that position array[i]

ex = [3,6,8,1,2]

at index 0, we can either take 1, 2 or 3 jumps forward
at index 1 we can take 1,2,3,4,5 or 6 jumps forward. We stop at the end of the array
"""


def min_jumps(array):
    jumps = [float("Inf")] * len(array)

    jumps[0] = 0  # 0 jumps required to reach the first element from the first element

    for i in range(len(array)):
        for j in range(i):
            if array[j] + j >= i:
                # we can jump directly from index i to index j
                jumps[i] = min(jumps[i], jumps[j] + 1)

    print(jumps)


def min_jumps_clever(array: "list[int]"):
    jumps = 0

    """  we can think of this as just traversing the array 1 element at a time and checking whether we should jump or just keep walking forward """
    steps = array[0]

    # max index we can reach when at a certain index
    max_reach = array[0]

    if max_reach == 0:
        return float("inf")

    for i in range(1, len(array) - 1):
        # at every index calculate the further distance we can reach from that index
        max_reach = max(max_reach, i + array[i])

        steps -= 1

        """
        if we exhaust our steps before reaching the max_reach, then it means
        that jumping at a previous index would've been better  
        """
        if steps == 0:
            jumps += 1
            steps = max_reach - i

    return jumps + 1


print(min_jumps_clever([5, 4, 2, 1, 2, 5, 7, 1, 1, 1, 3]))
