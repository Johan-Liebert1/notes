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

    def print_tree(self):
        import json

        print(
            json.dumps(
                self.root,
                indent=2,
            )
        )


s = SuffixTrie()

s.create("suffix")

s.print_tree()
