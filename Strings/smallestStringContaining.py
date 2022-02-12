"""  
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
"""


def smallest_substring_containing(string: str, substring: str) -> str:
    str_len = len(string)
    substring_chars: dict[str, int] = {}

    for char in substring:
        if char in substring_chars:
            substring_chars[char] += 1
        else:
            substring_chars[char] = 1

    left = 0
    right = -1
    left_idx = -1000
    right_idx = -1
    num_chars_found = 0
    found_chars_dict: dict[str, int] = {char: 0 for char in substring}

    while True:

        if num_chars_found == len(substring_chars):
            if right_idx - left_idx >= right - left:
                right_idx = right
                left_idx = left

            char_at_left = string[left]

            left += 1

            if char_at_left in substring_chars:
                found_chars_dict[char_at_left] -= 1
                num_chars_found -= 1
        else:
            right += 1

            if right == str_len:
                break

            char_at_right = string[right]

            if char_at_right in substring_chars:
                found_chars_dict[char_at_right] += 1

                if found_chars_dict[char_at_right] >= substring_chars[char_at_right]:
                    num_chars_found += 1

    return (string[left_idx : right_idx + 1],)


print(smallest_substring_containing("ADOBECODEBANC", "ABC"))
