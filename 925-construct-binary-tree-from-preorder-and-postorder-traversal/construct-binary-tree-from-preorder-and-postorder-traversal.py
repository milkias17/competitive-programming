# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        print(f"Pre: {preorder}, Post:{postorder}")
        cur = preorder.pop(0)
        root = TreeNode(cur)
        n = postorder.index(preorder[0]) if len(preorder) else -1

        root.left = self.constructFromPrePost(preorder[:n + 1], postorder[:n + 1])
        root.right = self.constructFromPrePost(preorder[n + 1:], postorder[n+1:len(postorder)-1])

        return root