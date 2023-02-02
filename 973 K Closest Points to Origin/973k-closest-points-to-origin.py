from math import sqrt

class Solution:
    def compute_distance(self, point: List[int]):
        return sqrt((point[0] ** 2) + (point[1] ** 2))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=self.compute_distance)[:k]