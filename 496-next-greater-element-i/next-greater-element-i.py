class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = {num: -1 for num in nums2}

        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            
            if len(stack) == 0:
                stack.append(nums2[i])
                continue
            
            result[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        return [result[i] for i in nums1]