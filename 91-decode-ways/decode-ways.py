class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i, memo={}):
            if i >= len(s):
                return 1
            
            if i in memo:
                return memo[i]
            
            count = 0
            if s[i] != "0":
                count += dfs(i + 1, memo)
            
            if i + 1 < len(s):
                if s[i] == "1":
                    count += dfs(i + 2, memo)
                elif s[i] == "2" and s[i + 1] <= "6":
                    count += dfs(i + 2, memo)

            memo[i] = count
            return count

        
        return dfs(0)