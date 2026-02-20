class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        queue = deque(sorted(points, key=lambda x: (x[1], x[0])))
        count = 0

        print(queue)
        while queue:
            taken = queue[0][1]
            count += 1
            while queue and taken >= queue[0][0] :
                queue.popleft()
        
        return count
