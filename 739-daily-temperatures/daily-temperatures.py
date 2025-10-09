class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            if len(stack) == 0:
                stack.append(i)
                continue
            
            cur = temperatures[i]
            while len(stack) > 0 and temperatures[stack[-1]] <= cur:
                stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                next_greater = stack[-1]
                answer[i] = next_greater - i
                stack.append(i)
        
        return answer