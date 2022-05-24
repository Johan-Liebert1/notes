"""
function returns a 2D array containing all the ways of constructing
the target_word by concatenating words in array. Each element of the 
2D array must give an combination of words, when concatenated, will 
form the target_word.

Words can be used as many times as needed
"""


def all_construct(target_word: str, array: list[str], memo: dict[str, str]) -> int:
    if target_word in memo:
        return memo[target_word]

    if target_word == "":
        return [[]]

    result = []

    for word in array:
        if target_word.startswith(word):

            suffix_ways = all_construct(target_word[len(word) :], array, memo)

            print(f"{suffix_ways = }, {word = }")

            # target ways is two dimensional
            target_ways = [[word] + i for i in suffix_ways]

            print(f"{target_ways = }, {word = }")

            # spread out target ways so that we don't nest things in too deep
            for way in target_ways:
                result.append(way)

    memo[target_word] = result
    return result


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
# print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))

# print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeee',
#                     ['ee', 'eee', 'eeeee', 'eeeeeee'], {}))
