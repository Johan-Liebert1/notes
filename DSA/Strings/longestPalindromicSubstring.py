def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break

        leftIdx -= 1
        rightIdx += 1

    return [leftIdx + 1, rightIdx]


"""  
loop over the original string and at each character, expand outwards to see if there's any palindrome
where that character is at the center. This works for odd length palindromes but not for even length
palindromes. 

To update the check for even length palindromes instead of making the current character the center,
we make the current character and it's left character to be at the center 
"""


def longestPalindormicSubstring(string):
    longest = [0, 1]

    for i in range(1, len(string)):
        # odd so no need to check the character at center as it's only one character
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)

        # even, so check current character and the character to its left
        even = getLongestPalindromeFrom(string, i - 1, i)

        print(f"{string[odd[0]:odd[1]] = }, { string[even[0]:even[1]] = }")

        longer = max(odd, even, key=lambda x: x[1] - x[0])

        longest = max(longer, longest, key=lambda x: x[1] - x[0])

    s, e = longest
    return string[s:e]


print(longestPalindormicSubstring("abaxyzzyxf"))
