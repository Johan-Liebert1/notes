from collections import defaultdict
import json
from typing import List
'''
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.


Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
'''


class WordFilter:

    def __init__(self, words: List[str]):
        self.dict = {"p": defaultdict(set), "s": defaultdict(set)}
        self.create_dict(words)
        print(json.dumps(self.dict))

    def create_dict(self, words):
        for index, word in enumerate(words):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                suffix = word[-i:]

                self.dict['p'][prefix].add(index)
                self.dict['s'][suffix].add(index)

    def f(self, prefix: str, suffix: str) -> int:

        prefix_indicies = self.dict['p'].get(prefix)
        suffix_indicies = self.dict['s'].get(suffix)

        if prefix_indicies is None or suffix_indicies is None:
            return -1

        return max(prefix_indicies & suffix_indicies)


words = ["cabaabaaaa", "ccbcababac", "bacaabccba"]
obj = WordFilter(words)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
