class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                memo[-1][i][j] = 0
        
        for i in range(len(strs) - 1, -1, -1):
            cur = strs[i]
            zero_count = cur.count("0")
            one_count = cur.count("1")

            for zeroes in range(m + 1):
                for ones in range(n + 1):
                    include = 0
                    if zero_count <= zeroes and one_count <= ones:
                        include = 1 + memo[i + 1][zeroes - zero_count][ones - one_count]
                    skip = memo[i + 1][zeroes][ones]
                    memo[i][zeroes][ones] = max(include, skip)
        
        return memo[0][m][n]
