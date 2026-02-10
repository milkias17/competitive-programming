class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_stack = []
        res = []
        for size in asteroids:
            if size > 0:
                right_stack.append(size)
                continue
            
            while right_stack and abs(size) > right_stack[-1]:
                right_stack.pop()
            
            if not right_stack:
                res.append(size)
            elif right_stack[-1] == abs(size):
                right_stack.pop()
        
        res.extend(right_stack)
        return res


