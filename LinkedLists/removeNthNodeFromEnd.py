
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        first = head
        second = head
        counter = 1

        while counter <= n:
            second = second.next
            counter = 1

        if not second:  # second is the null node, ie node to remove is the head node
            head = head.next
            return head

        while second.next:
            second = second.next
            first = first.next

        node_to_remove = first.next
        first.next = node_to_remove.next
        node_to_remove.next = None

        return head
