class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)

        # for i, num in enumerate(nums):
        for idx in range(len(nums) * 2):
            i = idx % len(nums)
            num = nums[i]
            while stack and num > nums[stack[-1]]:
                tmp = stack.pop()
                if res[tmp] == -1:
                    res[tmp] = i
            
            stack.append(i)
        
        for i in range(len(res)):
            if res[i] != -1:
                res[i] = nums[res[i]]

        return res

