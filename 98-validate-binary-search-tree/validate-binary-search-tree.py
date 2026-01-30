# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _is_valid(self, node, low=float("-inf"), high=float("inf")):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return self._is_valid(node.left, low, min(high, node.val)) and self._is_valid(node.right, max(low, node.val), high)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid(root)