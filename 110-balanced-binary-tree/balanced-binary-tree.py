# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _check_height(self, node):
        if node is None:
            return 0
        
        left = self._check_height(node.left)
        if left == -1:
            return -1
        right = self._check_height(node.right)
        if right == -1:
            return -1

        if abs(right - left) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self._check_height(root) != -1