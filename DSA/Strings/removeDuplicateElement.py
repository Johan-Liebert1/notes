"""  
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        seen_char = set()
        stack = []

        for c in s:
            if c not in freq:
                freq[c] = 0

            freq[c] += 1

        # use of a monotonic increasing stack

        for c in s:
            """
            iterate over s and push if the current character is
            lexicographically larger than the top most element on the stack
            as we want the final answer to be in lexicographic order

            on appending, decrease the frequency of the character to check
            whether the character will later appear in the string or not else
            we might end up popping a character that we'll never see again
            """

            freq[c] -= 1

            if c in seen_char:
                # already seen this character
                continue

            seen_char.add(c)

            while len(stack) > 0 and stack[-1] > c and freq[stack[-1]] > 0:
                # not in lexicographic order and we're sure to see the character later on
                # so pop the element from stack
                # also remove popped element from seen_char set

                seen_char.remove(stack.pop())

            stack.append(c)

        return "".join(stack)
