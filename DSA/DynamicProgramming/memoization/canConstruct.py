"""
function returns a bool indicating whether it is possible to 
get the target word from the strings in the array. Strings can
be used multiple times.
"""

# for some reason didn't need DP for this. This ran fast


def can_construct(target_word: str, array: "list[str]") -> bool:
    print(target_word)

    if target_word == "":
        return True

    can_do = False

    for string in array:
        if len(string) > 0 and target_word.startswith(string):
            can_do = can_do or can_construct(target_word[len(string) :], array)

    return can_do


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
