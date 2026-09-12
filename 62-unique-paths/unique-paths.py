class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (n)

        for r in range(m - 2, -1, -1):
            cur = [0] * (n)
            cur[n - 1] = 1
            for c in range(n - 2, -1, -1):
                res = dp[c] + cur[c + 1]
                cur[c] = res
            dp = cur
        
        return dp[0]
