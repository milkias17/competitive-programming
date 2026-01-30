# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0       

        def _height(node):
            if not node:
                return 0
            
            left = _height(node.left)
            right = _height(node.right)

            self.maxDiameter = max(self.maxDiameter, left + right)
            return max(left, right) + 1
        
        _height(root)
        return self.maxDiameter