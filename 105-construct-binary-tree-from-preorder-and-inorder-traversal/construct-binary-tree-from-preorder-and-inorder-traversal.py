# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        cur = preorder.pop(0)
        root = TreeNode(cur)
        idx = inorder.index(cur)

        root.left = self.buildTree(preorder[:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx:], inorder[idx + 1:])

        return root