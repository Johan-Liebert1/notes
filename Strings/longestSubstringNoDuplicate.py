"""  
Given a string S, find the longest substring in that string that does not have any duplicate
letter. 

Example : whatisthis | return whatisth
Example : coolcomputer | return lcomputer
"""


def longest_substring_no_duplicate(string: str):
    # { character: lastSeenIndex }
    hash_table = {}

    start_index = 0
    longest = [0, 1]

    for (i, char) in enumerate(string):
        if char in hash_table:
            start_index = max(hash_table[char] + 1, start_index)

        if longest[1] - longest[0] < i + 1 - start_index:
            longest = [start_index, i + 1]

        hash_table[char] = i

    return string[longest[0] : longest[1]]


print(longest_substring_no_duplicate("coolcomputer"))
