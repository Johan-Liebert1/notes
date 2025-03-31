def binary_tree_topologies(n: int, memo: "dict[int, int]"):
    """n = number of nodes"""
    if n < 2:
        return 1

    if n == 2:
        return 2

    if n in memo:
        return memo[n]

    total_topologies = 0

    for left_subtree_size in range(n):
        l = binary_tree_topologies(n - 1 - left_subtree_size, memo)
        r = binary_tree_topologies(left_subtree_size, memo)

        """  
        multiplying because for every topology of l, there can be a lot of topologies for r, and vice versa.
        """
        total_topologies += l * r

    memo[n] = total_topologies

    return total_topologies


print(binary_tree_topologies(50, {}))
