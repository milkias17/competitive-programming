class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        res = [-1] * len(graph)
        
        def dfs(i, color):
            if res[i] == color:
                return True

            if res[i] != -1:
                return False
            
            res[i] = color
            for neigh in graph[i]:
                if not dfs(neigh, 3 - color):
                    return False
            
            return True
        
        for i in range(len(graph)):
            if res[i] != -1:
                continue

            if not dfs(i, 1):
                return False
        
        return True

