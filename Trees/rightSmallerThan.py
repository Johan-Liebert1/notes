"""  
Given an array A, for every element find the number of elements to the right of the 
element that are strictly smaller than the current number

Example

A = [3,0,5,2]

sol = [2, 0, 1, 0]

Explanation 

3 has 2 elements smaller than itself to the right of it
0 has no elements smaller than itself to its right
5 has one smaller element to the right
2 has no element to its right
"""


class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1

            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime

            else:
                self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize

            if value > self.value:
                numSmallerAtInsertTime += 1

            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime

            else:
                self.right.insert(
                    value, idx, rightSmallerCounts, numSmallerAtInsertTime
                )


def right_smaller_than(array: "list[int]"):
    if len(array) == 0:
        return []

    right_smaller_counts = array[:]

    lastIndex = len(array) - 1

    bst = SpecialBST(lastIndex)

    right_smaller_counts[lastIndex] = 0

    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, right_smaller_counts)

    return right_smaller_counts
