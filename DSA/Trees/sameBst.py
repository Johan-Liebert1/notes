"""  
Given two arrays from with BSTs are to be created. Figure out whether the two arrays represent the same BST or not. You're not allowed to create a BST from the arrays
"""

# METHOD 1: Time - O(n^2) | Space - O(n^2)
def same_bsts_1(array1: "list[int]", array2: "list[int]"):
    # print(array1, array2)

    if len(array1) == 0 and len(array2) == 0:
        return True

    if len(array1) != len(array2) or array1[0] != array2[0]:
        return False

    # get the left and right subtrees, i.e. get all the elements smaller
    # than the root and all the ones larger than the root
    # don't include the root in the final array

    array1_smaller = [x for x in array1[1:] if x < array1[0]]
    array2_smaller = [x for x in array2[1:] if x < array2[0]]

    array1_larger = [x for x in array1[1:] if x >= array1[0]]
    array2_larger = [x for x in array2[1:] if x >= array2[0]]

    sm = same_bsts_1(array1_smaller, array2_smaller)
    lg = same_bsts_1(array1_larger, array2_larger)

    return sm and lg


# METHOD 1: Time - O(n^2) | Space - O(h) h = height of tree
def same_bsts_2(array1, array2):
    return check_bst_sameness(array1, array2, 0, 0, float("-Inf"), float("Inf"))


def check_bst_sameness(array1, array2, root_idx1, root_idx2, min_val, max_val):
    # root_idx is the index in the arrays where the current subtree's root is
    # min_val = minimum value that any node in the current subtree can have
    # max_val = maximum value that any node in the current subtree can have

    if root_idx1 == -1 or root_idx2 == -1:
        return root_idx1 == root_idx2

    if array1[root_idx1] != array2[root_idx2]:
        return False

    left_root_idx_1 = get_idx_of_first_smaller(array1, root_idx1, min_val)
    left_root_idx_2 = get_idx_of_first_smaller(array2, root_idx2, min_val)

    right_root_idx_1 = get_idx_of_first_bigger(array1, root_idx1, max_val)
    right_root_idx_2 = get_idx_of_first_bigger(array2, root_idx2, max_val)

    current_value = array1[root_idx1]

    left_are_same = check_bst_sameness(
        array1, array2, left_root_idx_1, left_root_idx_2, min_val, current_value
    )

    right_are_same = check_bst_sameness(
        array1, array2, right_root_idx_1, right_root_idx_2, current_value, max_val
    )

    return left_are_same and right_are_same


def get_idx_of_first_smaller(array, start_idx, min_value):
    for i in range(start_idx + 1, len(array)):
        if array[i] < array[start_idx] and array[i] >= min_value:
            return i

    return -1


def get_idx_of_first_bigger(array, start_idx, max_value):
    for i in range(start_idx + 1, len(array)):
        if array[i] >= array[start_idx] and array[i] < max_value:
            return i

    return -1


if __name__ == "__main__":
    print(
        same_bsts_2(
            [10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]
        )
    )
