class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(len(strs) - 1, -1, -1):
            new_dp = []
            count_0 = strs[i].count("0")
            count_1 = strs[i].count("1")
            for j in range(m + 1):
                tmp = []
                for k in range(n + 1):
                    res = dp[j][k]
                    if j - count_0 >= 0 and k - count_1 >= 0:
                        res = max(res, 1 + dp[j - count_0][k - count_1])
                    tmp.append(res)
                new_dp.append(tmp)
            
            dp = new_dp
        
        return dp[m][n]