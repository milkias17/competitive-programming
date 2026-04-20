class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(cur):
            if cur >= len(isConnected) or cur in visited:
                return
            
            visited.add(cur)
            for i in range(len(isConnected)):
                if isConnected[cur][i] == 1:
                    dfs(i)
        
        count = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            count += 1
            dfs(i)
        
        return count
            