class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        
        def dp(i, m, n):
            if i >= len(strs):
                return 0
            
            if (i, m, n) in memo:
                return memo[(i, m, n)]

            cur = strs[i]
            zero_count = cur.count("0")
            one_count = cur.count("1")

            include = 0
            if zero_count <= m and one_count <= n:
                include = 1 + dp(i + 1, m - zero_count, n - one_count)

            skip = dp(i + 1, m, n)
            
            memo[(i, m, n)] = max(include, skip)
            return max(include, skip)
        
        return dp(0, m, n)
            
