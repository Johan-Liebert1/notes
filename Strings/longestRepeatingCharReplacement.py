"""  
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


class Solution:
    # Time = O(n) | Space O(26)
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window technique
        left = 0
        most_freq_char_count = 1
        substr_len = 1

        hash_map = {}

        for right in range(len(s)):
            right_char = s[right]

            hash_map[right_char] = 1 + hash_map.get(right_char, 0)

            most_freq_char_count = max(most_freq_char_count, hash_map[right_char])

            # get the difference b/w the current window length and the
            # freq of most repeating character in that window. That's the
            # amount of replacements we can make

            # if replacements <= k:
            # we can replace characters
            while (right - left + 1) - most_freq_char_count > k:
                # number of replacements exceed the allowed amount of replacements
                # shrink the window from the left
                hash_map[s[left]] -= 1
                left += 1

            substr_len = max(substr_len, right - left + 1)

        return substr_len
