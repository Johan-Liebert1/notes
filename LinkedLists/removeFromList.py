'''
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
'''


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def removeKFromList(l, k):
    # print(l, l.value, l.next, l.next.value)
    start = l
    
    while start.next is not None:
        print(f"start.value, start.next = {start.value, start.next}")
        # print("inside while")
        pointToLNext = l.next
        print(f'pointToLNext.value = {pointToLNext.value}')

        if pointToLNext.value is not None:
            if pointToLNext.value == k:
                l.next = pointToLNext.next
                pointToLNext.next = None
                
        start = l.next
                
    return l            