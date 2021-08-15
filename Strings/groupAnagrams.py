from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:

    if len(strs) == 1:
        return [strs]

    dictionary = {}

    for element in strs:
        sorted_el = ''.join(sorted(element))

        if sorted_el not in dictionary:
            dictionary[sorted_el] = [element]

        else:
            dictionary[sorted_el].append(element)

    return list(dictionary.values())
