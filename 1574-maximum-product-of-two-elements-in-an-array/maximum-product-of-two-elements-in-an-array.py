class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_2 = []

        for num in nums:
            if len(max_2) < 2:
                heapq.heappush(max_2, num)
            elif max_2[0] < num:
                heapq.heapreplace(max_2, num)
        
        return (max_2[0] - 1) * (max_2[1] - 1)