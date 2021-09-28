"""  
literally like partition in quck sort. 
Given a linked list L, and an element in the linked list e, rearrange the LinkedList L inplace in such a way that all the elements smaller than e are the left of it and the rest are to the right.
Relative ordering of the elements is to be preserved
"""

from LinkedList import LinkedList, Node


def insert_into(head, tail, node):
    if not head:
        head = node
        return head, head

    tail.next = node

    return head, node


def rearrangeLinkedListMyMethod(head_node: Node, element: int):
    ptr = head_node

    smaller_head, equal_head, larger_head = [None] * 3
    smaller_tail, equal_tail, larger_tail = [None] * 3

    while ptr is not None:

        if ptr.value < element:
            smaller_head, smaller_tail = insert_into(smaller_head, smaller_tail, ptr)
        elif ptr.value == element:
            equal_head, equal_tail = insert_into(equal_head, equal_tail, ptr)
        else:
            larger_head, larger_tail = insert_into(larger_head, larger_tail, ptr)

        prevNode = ptr
        ptr = ptr.next
        prevNode.next = None

    if smaller_tail:
        smaller_tail.next = equal_head

    equal_tail.next = larger_head

    larger_tail = None

    return smaller_head if smaller_head else equal_head


# =========================== ALGO EXPERT METHOD ==============================


def rearrangeLinkedList(head, k):
    smallerListHead, equalListHead, greaterListHead = [None] * 3
    smallerListTail, equalListTail, greaterListTail = [None] * 3

    node = head

    while node is not None:
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(
                smallerListHead, smallerListTail, node
            )

        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(
                greaterListHead, greaterListTail, node
            )

        else:
            equalListHead, equalListTail = growLinkedList(
                equalListHead, equalListTail, node
            )

        prevNode = node
        node = node.next
        prevNode.next = None

    firstHead, firstTail = connectLinkedLists(
        smallerListHead, smallerListTail, equalListHead, equalListTail
    )
    finalHead, _ = connectLinkedLists(
        firstHead, firstTail, greaterListHead, greaterListTail
    )
    return finalHead


def growLinkedList(head, tail, node):
    newHead = head
    newTail = node

    if newHead is None:
        newHead = node

    if tail is not None:
        tail.next = node

    return (newHead, newTail)


def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:
        tailOne.next = headTwo

    return (newHead, newTail)


import random


def main():
    l_mine = LinkedList()
    l_other = LinkedList()

    ll = [random.randint(0, 100) for _ in range(0, random.randint(1, 10))]

    for i in ll:
        l_mine.insert(i)
        l_other.insert(i)

    target = ll[random.randint(0, len(ll) - 1)]

    l_mine.start = rearrangeLinkedListMyMethod(l_mine.start, target)
    l_other.start = rearrangeLinkedList(l_other.start, target)

    l_mine_traverse = l_mine.traverse()
    l_other_traverse = l_other.traverse()

    return l_mine_traverse == l_other_traverse


if __name__ == "__main__":
    for i in range(1000):
        l = []

        l.append(main())

    print(all(l))
