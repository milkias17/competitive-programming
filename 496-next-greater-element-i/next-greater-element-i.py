class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_idx_map = {}
        greater_prefix = [-1] * len(nums2)
        queue = deque()

        for i in range(len(nums2) - 1, -1, -1):
            num_idx_map[nums2[i]] = i
            while queue and nums2[i] > nums2[queue[-1]]:
                queue.pop()

            if queue:
                greater_prefix[i] = queue[-1]

            queue.append(i)
        
        res = []
        for num in nums1:
            tmp = greater_prefix[num_idx_map[num]]
            if tmp != -1:
                res.append(nums2[tmp])
            else:
                res.append(tmp)
        
        return res

        


