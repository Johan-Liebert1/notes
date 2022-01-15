"""  
A teacher has an array of student scores, and the teacher must purchase rewards to give to the students based on their score. The amount of rewards must follow 2 criteria:
Each student must have at least one reward.
The higher ranked student of two adjacent students must have more rewards than the other.
The goal is to find the minimum number of rewards to purchase
"""

# Time: O(n^2) | Space: O(n)
def min_rewards_naive(scores: "list[int]") -> list[int]:
    """
    approach 1 naive approach

    Iterate through the list and give every next item a value of 1 if it's smaller than the current item
    and then Iterate backwards to fix all the previous values
    """

    result = [0] * len(scores)

    result[0] = 1

    for i in range(1, len(scores)):
        if scores[i] < scores[i - 1]:
            result[i] = 1
            # iterate backwards and fix stuff
            for j in range(i - 1, -1, -1):
                if scores[j] < scores[j + 1]:
                    break

                result[j] = max(result[j], result[j + 1] + 1)
        else:
            result[i] = result[i - 1] + 1

    return result


# Time: O(n) | Space: O(n)
def min_rewards_minima_maxima_approach(scores: "list[int]") -> list[int]:
    """
    Find all the local minimas in the array. i.e. all the elements that are smaller than
    their left and right siblings. Then expand outwards from the local minimas and keep adding
    until you reach another local minima
    """
    pass


# Time: O(n) | Space: O(n)
def min_rewards_clever_approach(scores: "list[int]") -> list[int]:
    """
    similar to local minima maxima approach but no need to expand outwards or anything
    first iterate over the array from left to right and then iterate from right to left
    """

    result = [1] * len(scores)

    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]:
            result[i] = result[i - 1] + 1

    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            result[i] = max(result[i], result[i + 1] + 1)

    return result


lst = [8, 4, 2, 1, 3, 6, 7, 9, 5]

print(min_rewards_naive(lst), min_rewards_clever_approach(lst))
