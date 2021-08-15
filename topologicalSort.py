def topological_sort(array, dependencies):
    mapping = {}
    new_arr = [0] * len(array)

    for d in dependencies:
        first, second = d

        if first not in mapping:
            mapping[first] = [second]

        else:
            mapping[first].append(second)

    for job in array:
        pass


topological_sort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]])
