class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [len(word2) - j for j in range(len(word2) + 1)]

        for i in range(len(word1) - 1, -1, -1):
            new_dp = [len(word2) - j for j in range(len(word2) + 1)]
            new_dp[len(word2)] = len(word1) - i

            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    new_dp[j] = dp[j + 1]
                else:
                    new_dp[j] = 1 + min(dp[j + 1], dp[j], new_dp[j + 1])
            
            dp = new_dp

        return dp[0]