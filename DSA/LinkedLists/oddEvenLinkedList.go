package linkedlists

import "fmt"

// Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
//
// The first node is considered odd, and the second node is even, and so on.
//
// Note that the relative order inside both the even and odd groups should remain as it was in the input.
//
// You must solve the problem in O(1) extra space complexity and O(n) time complexity.

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil || head.Next.Next == nil {
		return head
	}

	var oddHead *ListNode = head
	var evenHead *ListNode = head.Next

	var originalOddHead *ListNode = oddHead
	var originalEvenHead *ListNode = evenHead

	ptr := evenHead.Next
	i := 1

	for ptr != nil {
        currentNext := ptr.Next

        fmt.Printf("oddHead: %d, evenHead: %d, ptr: %d, next: %p\n", oddHead.Val, evenHead.Val, ptr.Val, currentNext)

		// even
		if i == 0 {
			evenHead.Next = ptr
			evenHead = evenHead.Next
		} else {
			oddHead.Next = ptr
			oddHead = oddHead.Next
		}

		ptr = currentNext

		i = 1 - i
	}

    oddHead.Next = originalEvenHead

    evenHead.Next = nil

	return originalOddHead
}

func traverse(head *ListNode) {
    ptr := head

    for ptr != nil {
        fmt.Printf("ptr: %d\n", ptr.Val)
        ptr = ptr.Next
    }
}

func OddEvenList() {
    list := ListNode{
        Val: 1,
        Next: &ListNode{
            Val: 2,
            Next: &ListNode{
                Val: 3,
                Next: &ListNode{
                    Val: 4,
                    Next: &ListNode{
                        Val: 5,
                        Next: nil,
                    },
                },
            },
        },
    }

    traverse(&list)
    oddEvenList(&list)
    traverse(&list)
}

// 1, 2, 3, 4, 5
// oddHead = 1
// originalOddHead = 1
// evenHead = 2
// 
// ptr = 3
// currnext = 4
// 1 -> 3
// 
// oddHead = 3
// 
// ptr = 4
// evenHead = 2
// 2 -> 4
// evenHead = 4
// 
// ptr = 5
// next = nil
// 
// 3 -> 5



