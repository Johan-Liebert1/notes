package trees

func findNode(root, p *TreeNode) bool {
	if root == nil {
		return false
	}

	if root == p {
		return true
	}

	left := findNode(root.Left, p)

	if left {
		return true
	}

	return findNode(root.Right, p)
}

func lca(root, p, q *TreeNode) *TreeNode {
	if root == p || root == q {
		return root
	}

	isPOnLeft := findNode(root.Left, p)
	// P is on the left
	// then p has to be on the right as p does exist in the tree
	isQOnLeft := findNode(root.Left, q)

	if (isPOnLeft && !isQOnLeft) || (isQOnLeft && !isPOnLeft) {
		return root
	}

	if isPOnLeft && isQOnLeft {
		// we can ignore the entire right subtree
		return lca(root.Left, p, q)
	}

	return lca(root.Right, p, q)
}

func lowestCommonAncestorKindaSlow(root, p, q *TreeNode) *TreeNode {
	return lca(root, p, q)
}

// ======================== Fast but uses a little more memory ============================

func findPathToNode(root, node *TreeNode, path *[]*TreeNode) bool {
	if root == nil {
		return false
	}

	*path = append(*path, root)

	if root == node {
		return true
	}

	left := findPathToNode(root.Left, node, path)

	if left {
		return true
	}

	right := findPathToNode(root.Right, node, path)

	if !right && len(*path) >= 1 {
		*path = (*path)[:len(*path)-1]
	}

	return right
}

func lcaFast(root, p, q *TreeNode) *TreeNode {
	if root == p || root == q {
		return root
	}

	pathToP := []*TreeNode{root}
	findPathToNode(root.Left, p, &pathToP)

	// p was not on the left
	if len(pathToP) == 1 {
		// pathToP[0] = root.Right
		findPathToNode(root.Right, p, &pathToP)
	}

	pathToQ := []*TreeNode{root}
	findPathToNode(root.Left, q, &pathToQ)

	if len(pathToQ) == 1 {
		// pathToQ[0] = root.Right
		findPathToNode(root.Right, q, &pathToQ)
	}

	for i := range min(len(pathToP), len(pathToQ)) {
		if pathToP[i] != pathToQ[i] {
			return pathToP[i-1]
		}
	}

	if len(pathToP) < len(pathToQ) {
		return pathToP[len(pathToP)-1]
	}

	return pathToQ[len(pathToQ)-1]
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	return lcaFast(root, p, q)
}
