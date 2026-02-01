# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def helper(root):
            cur = root
            while cur:
                if not cur.left:
                    self.res.append(cur.val)
                    cur = cur.right
                    continue
                
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right

                if tmp.right == cur:
                    tmp.right = None
                    self.res.append(cur.val)
                    cur = cur.right
                else:
                    tmp.right = cur
                    cur = cur.left
        
        helper(root)
        return self.res
                
                
