class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for row in matrix:
            for el in row:
                if len(heap) < k:
                    heappush_max(heap, el)
                elif heap[0] > el:
                    heapreplace_max(heap, el)
        
        return heap[0]