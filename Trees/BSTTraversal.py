# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(f"{root.key} -> ", end=" ")

        # Traverse right
        inorder(root.right)


# preorder traversal
def preorder(root):
    if root is not None:
        # Traverse root
        print(f"{root.key} -> ", end=" ")

        # Traverse left
        preorder(root.left)

        # Traverse right
        preorder(root.right)


# postorder traversal
def postorder(root):
    if root is not None:
        # Traverse left
        postorder(root.left)

        # Traverse right
        postorder(root.right)

        # Traverse root
        print(f"{root.key} -> ", end=" ")


def iterative_preorder(root: Node):
    array = []
    stack: list[Node] = []
    current_node = root

    while len(stack) != 0 or current_node is not None:
        if current_node is not None:
            array.append(str(current_node.key))
            stack.append(current_node)

            # traverse the left tree
            current_node = current_node.left

        else:
            # current node is None
            current_node = stack.pop()
            current_node = current_node.right

    print(" ->  ".join(array))


def iterative_inorder(root: Node):
    array = []
    stack: list[Node] = []
    current_node = root

    while len(stack) != 0 or current_node is not None:
        if current_node is not None:
            stack.append(current_node)

            # traverse the left tree
            current_node = current_node.left

        else:
            # current node is None
            current_node = stack.pop()
            array.append(str(current_node.key))
            current_node = current_node.right

    print(" ->  ".join(array))


def iterative_postorder(root: Node):
    array = []
    stack: list[Node] = []
    right_child_stack: list[Node] = []
    current_node = root

    while len(stack) != 0 or current_node is not None:
        if current_node is not None:
            if current_node.right is not None:
                right_child_stack.append(current_node.right)

            stack.append(current_node)

            # traverse the left tree
            current_node = current_node.left

        else:
            # current node is None
            current_node = stack[-1]

            if (
                len(right_child_stack) != 0
                and current_node.right == right_child_stack[-1]
            ):
                current_node = right_child_stack.pop()

            else:
                array.append(str(current_node.key))
                stack.pop()
                current_node = None

    print(" ->  ".join(array))


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


s = """ 
                8
              /   \
             3    10
            / \     \
           1   6    14
              / \
             4   7 
"""

if __name__ == "__main__":
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)

    print("Inorder traversal: ", end=" ")
    inorder(root)
    print("\nIterative Inorder: ", end=" ")
    iterative_inorder(root)

    print()

    print("preorder traversal: ", end=" ")
    preorder(root)
    print("\nIterative preorder: ", end=" ")
    iterative_preorder(root)

    print()

    print("Postorder traversal: ", end=" ")
    postorder(root)
    print("\nIterative Postorder: ", end=" ")
    iterative_postorder(root)

    # print("\nDelete 10")
    # root = deleteNode(root, 10)
    # print("Inorder traversal: ", end=" ")
    # inorder(root)
