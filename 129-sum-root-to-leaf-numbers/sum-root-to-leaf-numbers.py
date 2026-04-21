# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur, cur_path):
            if not cur:
                return 0
            
            cur_path.append(str(cur.val))
            if not cur.left and not cur.right:
                val =  int("".join(cur_path))
                cur_path.pop()
                return val

            total = 0
            if cur.left:
                left = dfs(cur.left, cur_path)
                total += left
            if cur.right:
                right = dfs(cur.right, cur_path)
                total += right
            
            cur_path.pop()
            return total
        
        return dfs(root, [])
