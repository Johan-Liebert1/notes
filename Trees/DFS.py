class Node:
    def __init__(self, value):
        self.arr = []
        self.value = value


root = Node('A')
root.arr.push(Node('B'))
root.arr.push(Node('C'))
root.arr.push(Node('D'))

b = root.arr[0]
b.arr.push(Node('C'))
