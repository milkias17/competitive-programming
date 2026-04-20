class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        stack = [source]
        visited = set([source])
        while stack:
            cur = stack.pop()
            if cur == destination:
                return True
            for neigh in adj[cur]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                stack.append(neigh)
        
        return False
