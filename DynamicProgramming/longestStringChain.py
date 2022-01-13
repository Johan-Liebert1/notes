"""
given a list of strings find the longest string chain that can be made.
A string chain needs to have a minimum of 2 strings and is created by removing a letter from a word and if the
resulting word exists in the list then we have a string chain

ex 

array = [abc, de, ac]

longest string chain = abc, ac
reomving b from abc gives ac
"""


class Value:
    def __init__(self) -> None:
        self.computed = False
        self.longest_chain_len_starting = 0
        self.next_in_chain = ""

    def __repr__(self) -> str:
        return f"< computed: {self.computed}, longest: {self.longest_chain_len_starting}, next: {self.next_in_chain} >"


def calculate_string_chain(key: str, lookup: "dict[str, Value]"):
    max_chain_length = 0

    for i in range(len(key)):
        to_check = key[:i] + key[i + 1 :]

        if to_check in lookup:
            # a string found in the table after removing a letter from the current string
            if not lookup[to_check].computed:
                calculate_string_chain(to_check, lookup)

            if max_chain_length < 1 + lookup[to_check].longest_chain_len_starting:
                max_chain_length = 1 + lookup[to_check].longest_chain_len_starting
                lookup[key].next_in_chain = to_check

                print(
                    f"key = {key:<10},  to_check = {to_check:<10}, lookup[to_check] = {lookup[to_check]}"
                )

    lookup[key].computed = True
    lookup[key].longest_chain_len_starting = max_chain_length


def longest_string_chain(strings: "list[str]") -> "list[str]":
    return_array = []

    # [string]: whether a longest chain for this strings has been computed or not
    lookup: "dict[str, Value]" = {k: Value() for k in strings}

    for key in lookup.keys():
        calculate_string_chain(key, lookup)

    for key, val in lookup.items():
        print(f"{key:<10} {val}")


longest_string_chain(["abcde", "abde", "ae", "abcdef", "1abde", "abd", "abc", "ade"])
