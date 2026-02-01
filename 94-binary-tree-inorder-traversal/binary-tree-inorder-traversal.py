# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
                continue
            
            tmp = cur.left
            while tmp.right and tmp.right != cur:
                tmp = tmp.right

            if tmp.right == cur:
                tmp.right = None
                res.append(cur.val)
                cur = cur.right
            else:
                tmp.right = cur
                cur = cur.left
        
        return res
                
                
