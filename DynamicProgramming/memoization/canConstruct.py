'''
function returns a bool indicating whether it is possible to 
get the target word from the strings in the array. Strings can
be used multiple times.
'''

# for some reason didn't need DP for this. This ran fast


def can_construct(target_word, array):
    print(target_word)

    if target_word == "":
        return True

    i = 0

    while i < len(array):
        string = array[i]
        string_len = len(string)

        if string_len > 0 and target_word.startswith(string):
            return can_construct(target_word[string_len:], array)

        else:
            i += 1

    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
