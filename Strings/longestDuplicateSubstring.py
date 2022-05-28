from collections import defaultdict


class Solution:
    """
    This is a variation of longest common substring, we can solve it similar to LCS but space used will
    be massive.

    Also can solve this using Trie but is not most efficient

    1. Binary search on (1, len(s)) to find the longest repeating substring. If match found then try to find longer else find shorter. This will be our window

    2. Using Rabin-Karp hashing algo, find pattern of length = window

    3. Keep going until longest is found
    """

    def pattern_match(self, s: str, length: int, computed_array: "list[int]") -> bool:
        """
        use rabin karp algo to find patterns of len length and return true / false depending on
        whether there was a match or not

        'baa' = ( ( ( 2 * 26**2 ) % p + ( 1 * 26**1 ) ) % p + ( 1 * 26 ** 0 ) ) % p
        """

        hash_map = defaultdict(list)

        mod = 10000001

        hash_ = 0

        # calculate hash for the first window
        for i in range(length):
            hash_ = (hash_ * 26 + (ord(s[i]) - ord("a"))) % mod

        hash_map[hash_].append(0)

        # computing rolling hash here, so no need to keep adding hash
        for i in range(length, len(s)):
            hash_ = (
                (hash_ - computed_array[length - 1] * (ord(s[i - length]) - ord("a")))
                % mod
                + mod
            ) % mod

            # left shifting the hash
            hash_ = (hash_ * 26 + (ord(s[i]) - ord("a")) * 26 ** 0) % mod

            if hash_ in hash_map:
                for index in hash_map[hash_]:
                    string1 = s[index : index + length]
                    string2 = s[i - length + 1 : i + 1]

                    if string1 == string2:
                        return (True, string1)

            hash_map[hash_].append(i - length + 1)

        print(hash_map)

        return (False, "")

    def longestDupSubstring(self, s: str) -> str:
        if len(s) == 0:
            return ""

        low = 1
        high = len(s)
        longest_str = ""

        # {pattern of length n: [ indicies where the patterns start ]}
        computed_array = [26 ** i for i in range(len(s))]

        """  
        use binary search so that if string is of len 10, then we try to find longest repeating substring of length
        5, and if that exists then we try to find LRS of length > 5 and < 10 and so on
        """

        while low <= high:  # needs to be low <= high
            middle = (low + high) // 2

            match, string = self.pattern_match(s, middle, computed_array)

            if match:
                low = middle + 1
                longest_str = max(longest_str, string, key=lambda x: len(x))
            else:
                high = middle - 1

        return longest_str


def rabin_karp():
    s = "aaaaaa"

    h = 0

    for (index, char) in enumerate(s[:3]):
        h += 26 ** (2 - index) + (ord(s[index]) - ord("a") + 1)
        print(h)

    print(h)


print(
    Solution().longestDupSubstring(
        "nyvzwttxsshphczjjklqniaztccdrawueylaelkqtjtxdvutsewhghcmoxlvqjktgawwgpytuvoepnyfbdywpmmfukoslqvdrkuokxcexwugogcwvsuhcziwuwzfktjlhbiuhkxcreqrdbj"
    )
)

# rabin_karp()
