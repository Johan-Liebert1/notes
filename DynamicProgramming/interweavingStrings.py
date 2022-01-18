""" 
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

"""

# Time: O(2 ^ (n + m)) time
def interweaving_strings_no_cache(s1: str, s2: str, s3: str):
    if len(s3) != len(s1) + len(s2):
        return False

    return are_interwoven(s1, s2, s3, 0, 0)


def are_interwoven(s1: str, s2: str, s3: str, i: int, j: int):
    k = i + j

    if k == len(s3):
        return True

    if i < len(s1) and s1[i] == s3[k]:
        if are_interwoven(s1, s2, s3, i + 1, j):
            return True

    if i < len(s2) and s2[j] == s3[k]:
        return are_interwoven(s1, s2, s3, i, j + 1)

    return False


# Time: O(nm) | Space: O(nm)
def interweaving_strings_with_cache(s1: str, s2: str, s3: str):
    if len(s3) != len(s1) + len(s2):
        return False

    # having rows and cols as one more than length as
    # the index goes out of bounds so we want to keep track of that
    cache = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    return are_interwoven_cache(s1, s2, s3, 0, 0, cache)


def are_interwoven_cache(
    s1: str, s2: str, s3: str, i: int, j: int, cache: list[list[bool]]
):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j

    if k == len(s3):
        return True

    if i < len(s1) and s1[i] == s3[k]:
        cache[i][j] = are_interwoven_cache(s1, s2, s3, i + 1, j, cache)

        if cache[i][j]:
            return True

    if i < len(s2) and s2[j] == s3[k]:
        cache[i][j] = are_interwoven(s1, s2, s3, i, j + 1)

        return cache[i][j]

    cache[i][j] = False
    return False
