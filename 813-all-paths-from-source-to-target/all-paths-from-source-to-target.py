class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)

        def dfs(i, path, visited):
            path.append(i)
            if i == n - 1:
                paths.append(path.copy())
                path.pop()
                return

            visited.add(i)
            for neigh in graph[i]:
                if neigh not in visited:
                    dfs(neigh, path, visited)
            
            visited.remove(i)
            path.pop()
        
        dfs(0, [], set())
        return paths


