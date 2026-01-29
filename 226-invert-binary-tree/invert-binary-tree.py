# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _invert(self, node):
        if not node:
            return

        tmp = node.right
        node.right = node.left
        node.left = tmp
        self._invert(node.left)
        self._invert(node.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._invert(root)
        return root