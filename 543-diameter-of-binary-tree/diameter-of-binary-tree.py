# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _leaf_to_root(self, root):
        if root is None:
            return 0
        
        left = self._leaf_to_root(root.left)
        right = self._leaf_to_root(root.right)
        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diameter = 0
        self._leaf_to_root(root)

        return self.max_diameter
