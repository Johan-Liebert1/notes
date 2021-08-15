def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break

        leftIdx -= 1
        rightIdx += 1

    return [leftIdx + 1, rightIdx]


def longestPalindormicSubstring(string):
    longest = [0, 1]

    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)

        longer = max(odd, even, key=lambda x: x[1] - x[0])

        longest = max(longer, longest, key=lambda x: x[1] - x[0])

    s, e = longest
    return string[s:e]


print(longestPalindormicSubstring('abaxyzzyxf'))
