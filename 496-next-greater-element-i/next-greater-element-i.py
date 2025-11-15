class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_key_map = {}
        for i, num in enumerate(nums2):
            idx_key_map[num] = i
        
        output = []
        for num in nums1:
            idx = idx_key_map[num]
            if idx >= len(nums2) - 1:
                output.append(-1)
                continue

            val = -1
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > nums2[idx]:
                    val = nums2[i]
                    break
            
            output.append(val)
        
        return output