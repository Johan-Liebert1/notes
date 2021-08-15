class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, value):
        new_node = Node(value)

        if not self.top:  # first node
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        popped = self.top
        self.top = popped.next

        return popped.value


def check_balanced_brackets(brackets):
    s = Stack()

    mapping = {"(": ")", "[": "]",  "{": "}"}

    for b in brackets:
        prev_top = s.top
        s.push(b)

        if prev_top and prev_top.value in mapping:
            if mapping[prev_top.value] == b:
                s.pop()
                s.pop()

    return True if not s.top else False


print(check_balanced_brackets("([)]"))
