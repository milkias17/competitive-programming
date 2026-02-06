class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return 1

        heap = []
        for stone in stones:
            heappush_max(heap, stone)
        
        while len(heap) > 1:
            y = heappop_max(heap)
            x = heappop_max(heap)

            if x == y:
                continue
            
            heappush_max(heap, y - x)
        
        if len(heap) == 1:
            return heap[0]
        else:
            return 0

        
