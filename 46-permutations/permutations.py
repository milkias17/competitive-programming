class Solution:
    def create_permutations(self, nums: List[int], i):
        if i == len(nums):
            return
        
        self.create_permutations(nums, i + 1)
        new_perms = []
        for perm in self.perms:
            for j in range(len(perm) + 1):
                tmp = perm.copy()
                tmp.insert(j, nums[i])
                new_perms.append(tmp)
        
        self.perms = new_perms
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = [[]]
        self.create_permutations(nums, 0)
        return self.perms
