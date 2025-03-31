from typing import Dict, List


class Solution:

    def make_trie_graph(self, trie):
        s = "digraph { \n"

        def recurse(node, came_from_key, depth):
            nonlocal s
            if "*" in node:
                return

            for key in node:
                this_node_key = f"{came_from_key}{key}"
                this_node_value = f'"{this_node_key}" [label = {key}];'
                s += f"{this_node_value}\n"
                s += f'"{came_from_key}" -> "{this_node_key}"\n'

                recurse(node[key], this_node_key, depth + 1)

        recurse(trie, "root", 0)
        s += "}"

        with open("trie.dot", "w") as file:
            file.write(s)

    def make_prefix_trie(self, words: List[str]) -> Dict[str, str]:
        trie = {}

        for word in words:
            node = trie

            for i in range(len(word)):
                char = word[i]

                if char not in node:
                    node[char] = {}
                node = node[char]

            node["*"] = True

        return trie

    def create_rest_of_the_word(self, node, word, result):

        for key in node:
            if key == '*':
                result.append(word)
                continue

            word += key
            self.create_rest_of_the_word(node[key], word, result)
            word = word[:-1]

    def search_in_trie(self, trie: Dict[str, str],
                       search_word: str) -> List[str]:
        result = []

        word = ""
        node = trie

        for char in search_word:
            if char not in node:
                continue

            word += char

            if '*' in node:
                # word ends here
                result.append(word)

            node = node[char]

            if not isinstance(node, dict):
                break

        self.create_rest_of_the_word(node, word, result)
        return result

    def suggestedProducts(self, products: List[str],
                          searchWord: str) -> List[List[str]]:
        result_list: List[List[str]] = []
        trie = self.make_prefix_trie(products)

        self.make_trie_graph(trie)
        search_string = ""

        for character in searchWord:
            search_string += character
            result = self.search_in_trie(trie, search_string)
            result_list.append(sorted(result)[:3])

        return result_list


print(Solution().suggestedProducts(
    ["bags", "baggage", "banner", "box", "cloths"], 'bags'))
