class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, visited):
            if node == destination:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adj[node]:
                if dfs(neigh, visited):
                    return True
            
            return False
        
        return dfs(source, set())