class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        i = 0
        res = 0

        while i < len(answers):
            cur = answers[i]
            tmp = cur
            
            i += 1
            while tmp > 0 and i < len(answers) and answers[i] == cur:
                tmp -= 1
                i += 1
            
            res += cur + 1
        
        return res