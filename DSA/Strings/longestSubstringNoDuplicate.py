"""  
Given a string S, find the longest substring in that string that does not have any duplicate
letter. 

Example : whatisthis | return whatisth
Example : coolcomputer | return lcomputer
"""


"""  
solving this with the sliding window technique. let's say string is abcabcbb

at a fine (starting at 0 a) substring = a
at b fine | substring = ab
at c fine | substring = abc
at a (we have an a alredy so shrink from the left, now starting at 1 b) | substring = bca

at b (shrink again starting at 2 c) substring is cab
at c (shrink again starting at 3 a) | substring = abc

at b (current substring = abcb) we cannot just shrink once we have to shrink twice, so keep track of the latest index
of a certain character so we can just shrink upto that character

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
