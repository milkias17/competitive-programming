class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones.copy()
        heapify_max(heap)

        while len(heap) > 1:
            y = heappop_max(heap)
            x = heappop_max(heap)

            if x != y:
                heappush_max(heap, y - x)
        
        return 0 if len(heap) == 0 else heap[0]
