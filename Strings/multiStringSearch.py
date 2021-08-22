""" 
Given a string S, and an array of strings[], return a boolean array where every element
at index i, corresponds to whether the string at strings[i] is contained in the big string S or not

ex 
S = "this is a big string"
strings = ["this", "ha", "is", "bigger", "lmao", "str"]

output = [T, F, T, F, F, T]

Sol 1 - naive - okayish
Sol 2 - create a suffix trie from the string S - better
Sol 3 - create a suffix trie from the strings in strings[] array - best
"""


class SuffixTrie:
    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "$"

    def add_word(self, string: str):
        """add the entire string and not all just the suffix"""
        current_node = self.root

        for s in string:
            if s in current_node:
                current_node = current_node[s]
                continue

            current_node[s] = {}
            current_node = current_node[s]

        current_node[
            self.end_symbol
        ] = string  # so that we won't have to slice the string at line 72

    # def

    def print_tree(self):
        import json

        print(
            json.dumps(
                self.root,
                indent=2,
            )
        )


def multi_string_search(string: str, strings_array: "list[str]"):
    trie = SuffixTrie()

    array = [False] * len(strings_array)

    for s in strings_array:
        trie.add_word(s)

    found_strings = {}

    for i in range(len(string)):
        current_node = trie.root

        for j in range(i, len(string)):
            if string[j] not in current_node:
                break

            current_node = current_node[string[j]]

            if trie.end_symbol in current_node:
                found_strings[current_node[trie.end_symbol]] = True

    for i in range(len(strings_array)):
        s = strings_array[i]

        if s in found_strings:
            array[i] = True

    print(array, found_strings)

    return array


multi_string_search(
    "this is a big string", ["this", "ha", "is", "bigger", "lmao", "str"]
)
