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
    """  
    dist travelled by first = d + p (d = unlooped part, p = looped part)
    dist travelled by second = 2 * first = 2d + 2p (as second is skipping a node)

    total dist = t; dist from final overlap of first and second to the loop start = r

    t = d + p + r or 2d + 2p - p (as second has looped over once more) = 2d + p

    r = t - d - p = 2d + p - p - d = d
    r = d;

    thus we reset f, and move both one forward so they'll intersect as now they'll both be same distance from the loop
    """

    first = head

    while second != first:
        second = second.next
        first = first.next

    return first
