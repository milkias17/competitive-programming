# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        per_height = defaultdict(list)

        queue = deque()
        if root:
            queue.append((root, 0))

        while queue:
            cur, height = queue.popleft()
            per_height[height].append(cur.val)

            if cur.left:
                queue.append((cur.left, height + 1))
            if cur.right:
                queue.append((cur.right, height + 1))
        
        res = [-1] * (max(per_height.keys()) + 1)
        for k, v in per_height.items():
            res[k] = v

        return res