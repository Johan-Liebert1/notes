from typing import Union


class Node:
    def __init__(self, value: int) -> None:
        self.next: Union[None, Node] = None
        self.value: int = value


class LinkedList:
    def __init__(self) -> None:
        self.start = None

    def insert(self, value: int):
        node = Node(value)

        if not self.start:
            self.start = node
            return self

        ptr = self.start

        while ptr.next is not None:
            ptr = ptr.next

        ptr.next = node

        return self

    def traverse(self):
        string = ""

        ptr = self.start

        while ptr is not None:
            string += f"{ptr.value} -> "
            ptr = ptr.next

        # print(string[:-4])

        return string[:-4]


if __name__ == "__main__":
    ll = LinkedList()

    for i in range(1, 11):
        ll.insert(i)

    ll.traverse()
