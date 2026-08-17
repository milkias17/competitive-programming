class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 if j != len(t) else 1 for j in range(len(t) + 1)]
        for i in range(len(s) - 1, -1, -1):
            nxt = [0] * (len(t) + 1)
            nxt[len(t)] = 1
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    nxt[j] = dp[j + 1] + dp[j]
                else:
                    nxt[j] = dp[j]
            dp = nxt
        
        return dp[0]