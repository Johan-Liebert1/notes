// In a linked list of size n, where n is even, the ith node (0-indexed)
// of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
//
// For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
// The twin sum is defined as the sum of a node and its twin.
//
// Given the head of a linked list with even length, return the maximum twin sum of the linked list.

package linkedlists

func pairSum(head *ListNode) int {
	if head.Next.Next == nil {
		return head.Val + head.Next.Val
	}

	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	fast = slow.Next

	// Reverse the linked list
	for fast != nil {
		nextFast := fast.Next

		fast.Next = slow

		slow = fast
		fast = nextFast
	}

	// slow is at the end

	fast = head

	m := 0

	for {
		s := fast.Val + slow.Val

		if s > m {
			m = s
		}

		if fast.Next == slow {
			break
		}

		fast = fast.Next
		slow = slow.Next
	}

	return m
}
