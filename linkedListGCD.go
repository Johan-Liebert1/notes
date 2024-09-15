package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func getGCD(a int, b int) int {
	if a == 0 || b == 0 {
		return max(a, b)
	}

	for {
		if a == b {
			break
		}

		if a > b {
			a -= b
		} else {
			b -= a
		}
	}

	return b
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	var current *ListNode = head

	for {
		if current == nil || current.Next == nil {
			break
		}

		gcd := getGCD(current.Val, current.Next.Val)

        prevNext := current.Next

		current.Next = &ListNode{
			Val:  gcd,
			Next: current.Next,
		}

        current = prevNext
	}

	return head
}
