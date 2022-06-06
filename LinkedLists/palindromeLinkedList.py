"""  
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
"""


from pyparsing import Optional
from LinkedList import Node


class Solution:
    # optimal Solution
    def isPalindrome(self, head: Optional[Node]) -> bool:
        """
        1. One slow pointer that moves 1 step forward
        2. One fast pointer that moves 2 steps forward
        3. at the end fast pointer is at the end of the list and the slow one is at the middle of the list

        4. no we just need to go left with the slow pointer and right with the fast pointer
        5. Since we can't go back with pointers, we'll keep reversing the list with the slow pointer such that
        1st half of the list is reversed while the second half is not reversed
        """

        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev:
            if slow.val != rev.val:
                return False
            else:
                slow, rev = slow.next, rev.next
        return not rev

    # Naive Solution
    def isPalindrome(self, head: Optional[Node]) -> bool:
        s = ""

        ptr = head

        while ptr:
            s += str(ptr.val)
            ptr = ptr.next

        if len(s) < 2:
            return True

        end = len(s) // 2
        next_start = end if len(s) % 2 == 0 else end + 1

        return s[:end][::-1] == s[next_start:]
