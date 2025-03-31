'''
Given an array strings, determine whether it follows the sequence given in the patterns array. 
In other words, there should be no i and j for which 
strings[i] = strings[j] and patterns[i] ≠ patterns[j] 
or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.'''
from tests import s, p
# s = ["cat", "dog", "dog"]
# p = ["a", "b", "c"]

def areFollowingPatterns(strings, patterns):
    # two dictionaries as stings and patterns can have the same string, and they can collide
    string_to_pattern = {} 
    pattern_to_string = {}

    for i in range(len(strings)):
        current_str = strings[i]
        current_ptr = patterns[i]

        if current_str not in string_to_pattern:
            string_to_pattern[current_str] = [current_ptr]

        if current_ptr not in pattern_to_string:
            pattern_to_string[current_ptr] = [current_str]

        # else: # current_str is already present and current_ptr is also present

        if current_ptr not in string_to_pattern[current_str]:
            return False

        if current_str not in pattern_to_string[current_ptr]:
            return False

    return True


print(areFollowingPatterns(s, p))
        