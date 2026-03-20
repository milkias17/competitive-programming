# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode], cur_path=[]) -> int:
        if not root:
            return 0
        
        tmp = 0
        if len(cur_path) >= 2:
            parent = cur_path[-2]
            if parent % 2 == 0:
                tmp += root.val
        
        cur_path.append(root.val)
        left = self.sumEvenGrandparent(root.left, cur_path)
        right = self.sumEvenGrandparent(root.right, cur_path)
        cur_path.pop()
        return tmp + left + right
        

        