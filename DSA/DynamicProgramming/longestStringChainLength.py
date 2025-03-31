"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
"""

from typing import List
import heapq


class Solution:

    def can_make_word_from_word(self, use_word: str, make_word: str):
        i, j = 0, 0

        while i < len(use_word) and j < len(make_word):
            if use_word[i] != make_word[j]:
                j += 1
                continue

            i += 1
            j += 1

        return i == len(use_word)

    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1

        d = {}

        for w in words:
            if len(w) in d:
                d[len(w)].append(w)
            else:
                d[len(w)] = [w]

        heapq.heapify(words)

        max_chain_len = 1

        # word -> Longest chain made using that word
        cache = {}

        def dfs(current_smallest_word):
            nonlocal max_chain_len

            if current_smallest_word in cache:
                return cache[current_smallest_word]

            if len(current_smallest_word) + 1 not in d:
                cache[current_smallest_word] = 1
                return 1

            maxx = 1

            for word in d[len(current_smallest_word) + 1]:
                # these are all the words that have one more letter than the current word
                if self.can_make_word_from_word(current_smallest_word, word):
                    maxx = max(maxx, 1 + dfs(word))

            cache[current_smallest_word] = maxx
            max_chain_len = max(max_chain_len, maxx)

            return maxx

        while len(words) > 0:
            current_smallest = heapq.heappop(words)

            if current_smallest in cache:
                continue

            if len(current_smallest) + 1 not in d:
                continue

            # if word already in some chain, then don't call it
            dfs(current_smallest)

        return max_chain_len
