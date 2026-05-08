class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            
            heappush(heap, heights[i + 1] - heights[i])
            if len(heap) > ladders:
                lowest_gap = heappop(heap)
                bricks -= lowest_gap

                if bricks < 0:
                    return i
        
        return len(heights) - 1


