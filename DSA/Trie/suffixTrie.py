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

            current_node = current_node[current_letter]

        current_node[self.end_char] = True

    def make_trie_graph(self):
        s = "digraph { \n"

        def recurse(node, came_from_key, depth):
            nonlocal s

            for key in node:
                if key == '*':
                    continue

                this_node_key = f"{came_from_key}{key}"
                this_node_value = f'"{this_node_key}" [label = {key}];'
                s += f"{this_node_value}\n"
                s += f'"{came_from_key}" -> "{this_node_key}"\n'

                recurse(node[key], this_node_key, depth + 1)

        recurse(self.root, "root", 0)
        s += "}"

        with open("trie.dot", "w") as file:
            file.write(s)


s = SuffixTrie()

s.create("suffix")
s.create("moresuffix")
s.create("suffixtrie")

s.make_trie_graph()

import json

print(json.dumps(s.root))
