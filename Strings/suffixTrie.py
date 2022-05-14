class SuffixTrie:
    def __init__(self) -> None:
        self.root = {}
        self.end_char = "*"

    def create(self, string: str):
        for i in range(len(string)):
            self.insert_into_trie(i, string)

    def insert_into_trie(self, index: int, string: str):
        current_node = self.root

        for i in range(index, len(string)):
            current_letter = string[i]

            if current_letter not in current_node:
                current_node[current_letter] = {}

            print(f"{current_node = }")
            print(f"{current_node[current_letter] = }\n\n")

            current_node = current_node[current_letter]

        current_node[self.end_char] = True

    def print_tree(self):
        import json

        print(
            json.dumps(
                self.root,
                indent=2,
            )
        )

    def tree_graph(self, root: dict[str, str], s: list[str], parent="0", depth=0):
        if type(root) == bool:
            return

        for key, value in root.items():
            print(f"{key = }, {value = }")

            s[0] += f'{parent}-{depth} [label = "{parent}"]'
            s[0] += f"{parent}-{depth} -> {key} \n"

            self.tree_graph(value, s, key, depth + 1)


s = SuffixTrie()

s.create("suffix")

s.print_tree()

# print(s.root)


# l = ["digraph {\n"]

# l[0] += ""

# s.tree_graph(s.root, l)


# l[0] += "}"

# with open("trie.dot", "w") as trie:
#     trie.write(l[0])

# import os

# os.system("dot -T svg trie.dot > trie.svg && brave trie.svg")
