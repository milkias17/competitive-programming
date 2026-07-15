class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for k in range(len(s3) - 1, -1, -1):
            new_dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

            for i in range(len(s1), -1, -1):
                for j in range(len(s2), -1, -1):
                    if i < len(s1) and s1[i] == s3[k] and dp[i + 1][j]:
                        new_dp[i][j] = True
                    elif j < len(s2) and s2[j] == s3[k] and dp[i][j + 1]:
                        new_dp[i][j] = True
            
            dp = new_dp


        return dp[0][0]
            

                