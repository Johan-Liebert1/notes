"""
function returns a number indicating the number of ways it is possible to 
get the target word from the strings in the array. Strings can
be used multiple times.
"""


def count_construct(target_word, array, memo) -> int:
    if target_word in memo:
        return memo[target_word]

    if target_word == "":
        return 1

    total_ways = 0
    for word in array:
        if target_word.startswith(word):
            total_ways += count_construct(target_word[len(word) :], array, memo)

    memo[target_word] = total_ways
    return total_ways


print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeeee", "eeeeee"],
        {},
    )
)
