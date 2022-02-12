def permutations(array: list[int], permutations_array: list[int]):
    if len(array) == 1:
        return [array.copy()]
