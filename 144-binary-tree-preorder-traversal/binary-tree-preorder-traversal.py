# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _helper(self, root):
        if not root:
            return
        
        self.arr.append(root.val)
        self._helper(root.left)
        self._helper(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self._helper(root)
        return self.arr