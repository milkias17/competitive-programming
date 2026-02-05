class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            next_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    tmp = perm.copy()
                    tmp.insert(i, num)
                    next_perms.append(tmp)
            
            perms = next_perms
        
        return perms
