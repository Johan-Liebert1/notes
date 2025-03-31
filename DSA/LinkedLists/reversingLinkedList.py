'''sansad bighatan'''


class Solution:
    def reverseList(self, head):
        if not head:
            return

        if not head.next:
            return head

        p1, p2, p3 = None, None, None

        p1 = head
        p2 = head.next

        if p2.next:
            p3 = p2.next

        while 1:
            p2.next = p1

            if not p3:
                break

            if not p2:
                break

            p1 = p2
            p2 = p3
            p3 = p3.next

        head.next = None
        head = p2

        return head
