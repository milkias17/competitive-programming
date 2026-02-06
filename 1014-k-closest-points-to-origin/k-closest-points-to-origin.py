from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            point_distance = sqrt(x ** 2 + y ** 2)
            if len(heap) < k:
                heappush_max(heap, (point_distance, point))
            else:
                worst = heap[0]
                if point_distance < worst[0]:
                    heappop_max(heap)
                    heappush_max(heap, (point_distance, point))
        
        return [point for distance, point in heap]