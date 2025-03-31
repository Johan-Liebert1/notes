package binarytrees

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// func deleteFoundNode(root *TreeNode) {
// 	deleteFoundNode(newRoot)
// }

func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return root
	}

	if key < root.Val {
		root.Left = deleteNode(root.Left, key)
	} else if key > root.Val {
		root.Right = deleteNode(root.Right, key)
	} else {
		// root only has right child
		if root.Right == nil {
			return root.Left
		}

		// root only has left child
		if root.Left == nil {
			return root.Right
		}

        // the above two cases also handle leaf nodes
        // if root.Right == nil then root.left will also be nil, and vice-versa

		// root has both children

		// Get the largest value in the left subtree
		// OR, get the smallest value in the right subtree
		// then replace root with it

		// We'll get the largest value in the left subtree
		newRoot := root.Left

		for newRoot.Right != nil {
			newRoot = newRoot.Right
		}

		root.Val = newRoot.Val

		root.Left = deleteNode(root.Left, newRoot.Val)
	}

	return root
}
