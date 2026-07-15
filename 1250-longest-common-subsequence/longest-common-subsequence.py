class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [0] * (len(text2) + 1)
        
        for i in range(len(text1) - 1, -1, -1):
            new_memo = [0] * (len(text2) + 1)
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    new_memo[j] = 1 + memo[j + 1]
                else:
                    new_memo[j] = max(memo[j], new_memo[j + 1])
            memo = new_memo
        
        return memo[0]
            
