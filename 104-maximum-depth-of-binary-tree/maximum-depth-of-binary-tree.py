# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], acc=0) -> int:
        if not root:
            return acc
        
        left_depth = self.maxDepth(root.left, acc + 1)
        right_depth = self.maxDepth(root.right, acc + 1)

        return max(left_depth, right_depth)