class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        def dfs(cur, color):
            if colors[cur] != -1:
                if colors[cur] == color:
                    return True

                return False

            colors[cur] = color
            for neighbor in graph[cur]:
                if not dfs(neighbor, 3 - color):
                    return False
            
            return True
            
        for i in range(len(graph)):
            if colors[i] != -1:
                continue
                
            if not dfs(i, 1):
                return False
        return True