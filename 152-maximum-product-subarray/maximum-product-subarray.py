class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix_right = [[None, None] for _ in range(len(nums) + 1)]
        
        for i in range(len(nums) - 1, -1, -1):
            cur = nums[i]
            max_pos, max_neg = prefix_right[i + 1]

            if cur < 0:
                prefix_right[i][0] = cur * max_neg if max_neg is not None else None
                prefix_right[i][1] = cur * max_pos if max_pos else cur
            else:
                prefix_right[i][0] = cur * max_pos if max_pos else cur
                prefix_right[i][1] = cur * max_neg if max_neg is not None else None
        
        print(prefix_right)
        max_val = float("-inf")
        for pos, neg in prefix_right:
            if pos is None and neg is None:
                continue
            
            tmp = None
            if pos is None:
                tmp = neg
            else:
                tmp = pos
            
            max_val = max(max_val, tmp)
            

        return max_val