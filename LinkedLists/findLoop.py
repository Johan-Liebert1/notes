# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# there may or may not be a loop
def detectCycle(head):
    first = head
    second = head

    if not first or not first.next:  # no node or only one node
        return None

    while second and second.next:
        if not second.next.next:
            return None

        second = second.next.next
        first = first.next

        if second == first:
            break

    if not second.next:  # we reached the end and there was no loop
        return None

    first = head

    while second != first:
        second = second.next
        first = first.next

    return first
