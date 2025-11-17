import math
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = []
        for i, ball in enumerate(boxes):
            if ball == '1':
                balls.append(i)
        
        answer = []
        for i, box in enumerate(boxes):
            steps = 0
            for ball in balls:
                if ball == i:
                    continue
                steps += abs(ball - i)
            answer.append(steps)
        
        return answer