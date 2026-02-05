class Solution:
    def create_permutations(self, nums: List[int], cur_perms: List[List[int]], perms: List[List[int]]):
        print(f"Cur: {cur_perms}")
        if len(nums) == 0:
            new_copy = []
            for perm in cur_perms:
                perms.append(perm.copy())
            return
        
        for i, num in enumerate(nums):
            for perm in cur_perms:
                perm.append(num)
                nums_copy = nums.copy()
                nums_copy.pop(i)
                self.create_permutations(nums_copy, cur_perms, perms)
                perm.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.create_permutations(nums, [[]], perms)
        return perms
        
