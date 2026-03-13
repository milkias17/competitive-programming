class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        count = 0
        i = 0

        # print(points)
        while i < len(points):
            point = points[i]
            hit = point[1]

            while i < len(points) and hit >= points[i][0] and hit <= points[i][1]:
                i += 1
            
            count += 1
        return count


