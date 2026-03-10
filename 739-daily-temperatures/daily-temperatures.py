class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = deque()
        answer = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while queue and temperatures[queue[-1]] < temperature:
                idx = queue.pop()
                answer[idx] = i - idx
            
            queue.append(i)
        
        return answer