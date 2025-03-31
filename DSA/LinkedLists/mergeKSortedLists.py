# Definition for singly-linked list.


from typing import List

from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # We can collect all the values of the LinkedList into a minheap
        # we can pop every time from the minheap
        # the heap is already sorted so everytime it will give us the smallest value
        import heapq

        res = []

        for ll in lists:
            curr = ll
            while curr:
                heapq.heappush(res, curr.val)
                curr = curr.next

        head = ListNode(0)
        curr = head

        while len(res):
            curr_val = heapq.heappop(res)
            curr.next = ListNode(curr_val)
            curr = curr.next

        return head.next


# My approach
class Solution:
    def update_pointers(self, ptr_into_lists):
        i = -1
        minimum = float("inf")

        for (index, list_ptr) in enumerate(ptr_into_lists):
            if list_ptr is not None and list_ptr.val < minimum:
                i = index
                minimum = list_ptr.val

        return i

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        head = None
        ptr = None

        ptr_into_lists = [l for l in lists]

        while True:
            min_element_index = self.update_pointers(ptr_into_lists)

            if min_element_index == -1:
                break

            new_node = ListNode(ptr_into_lists[min_element_index].val)

            ptr_into_lists[min_element_index] = ptr_into_lists[min_element_index].next

            if head is None:
                head = new_node
                ptr = head
            else:
                ptr.next = new_node
                ptr = new_node

        return head
