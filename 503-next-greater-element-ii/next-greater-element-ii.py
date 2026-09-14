class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double = nums.copy()
        double.extend(nums[:len(nums) - 1])

        stack = []
        ans = [-1] * len(nums)
        for i, num in enumerate(double):
            while stack and num > double[stack[-1]]:
                idx = stack.pop() % len(nums)
                if ans[idx] == -1:
                    ans[idx] = num
            
            stack.append(i)
        
        return ans
                