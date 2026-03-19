/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func helper(cur *TreeNode, acc int) int {
    if cur == nil {
        return acc
    }

    left := helper(cur.Left, acc + 1)
    right := helper(cur.Right, acc + 1)

    if left > right {
        return left
    }

    return right
}

func maxDepth(root *TreeNode) int {
    return helper(root, 0)
}