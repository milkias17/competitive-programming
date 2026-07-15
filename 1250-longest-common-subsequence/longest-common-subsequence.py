class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for j in range(len(text2) + 1):
            memo[len(text1)][j] = 0
        
        for i in range(len(text1) + 1):
            memo[i][len(text2)] = 0
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i + 1][j + 1]
                else:
                    memo[i][j] = max(memo[i + 1][j], memo[i][j + 1])
        
        return memo[0][0]
            
