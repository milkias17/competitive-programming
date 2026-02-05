class Solution:
    def create_permutations(self, nums: List[int], cur_perms: List[List[int]], perms: List[List[int]]):
        if len(nums) == len(self.discluded):
            for perm in cur_perms:
                perms.append(perm.copy())
            return
        
        for i, num in enumerate(nums):
            if i in self.discluded:
                continue
                
            for perm in cur_perms:
                perm.append(num)
                self.discluded.add(i)
                self.create_permutations(nums, cur_perms, perms)
                perm.pop()
                self.discluded.remove(i)


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.discluded = set()
        perms = []
        self.create_permutations(nums, [[]], perms)
        return perms
        
