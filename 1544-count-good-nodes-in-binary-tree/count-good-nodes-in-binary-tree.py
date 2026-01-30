# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, node: TreeNode, max_val=float("-inf")):
        if not node:
            return

        if node.val >= max_val:
            self.good += 1
        
        self.postorder(node.left, max_val=max(max_val, node.val))
        self.postorder(node.right, max_val=max(max_val, node.val))
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.postorder(root)
        return self.good