class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return self

        q = [self.root]

        while len(q) > 0:
            current_node = q[0]

            if not current_node.left:
                current_node.left = node
                break

            if not current_node.right:
                current_node.right = node
                break

            q.append(current_node.left)
            q.append(current_node.right)

            q = q[1:]

        return self

    def traverse(self):
        array = []

        if not self.root:
            print("Tree is empty")
            return

        q = [self.root]

        while len(q) > 0:
            current_node = q[0]

            array.append(current_node.value)

            if current_node.left:
                q.append(current_node.left)

            if current_node.right:
                q.append(current_node.right)

            q = q[1:]

        print(array)


if __name__ == "__main__":
    tree = BinaryTree()

    for i in range(1):
        tree.insert(i)

    tree.traverse()
