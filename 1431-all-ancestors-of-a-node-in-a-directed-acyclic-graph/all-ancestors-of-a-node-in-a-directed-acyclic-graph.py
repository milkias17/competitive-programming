class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for i in range(n)]

        adj = {i: [] for i in range(n)}
        in_order = {i: 0 for i in range(n)}

        for src, dest in edges:
            adj[src].append(dest)
            in_order[dest] += 1
        
        queue = deque([k for k, v in in_order.items() if v == 0])

        while queue:
            cur = queue.popleft()

            for neigh in adj[cur]:
                # answer[neigh].append(cur)
                answer[neigh].add(cur)
                for tmp in answer[cur]:
                    answer[neigh].add(tmp)
                in_order[neigh] -= 1
                if in_order[neigh] <= 0:
                    queue.append(neigh)
        
        for i in range(n):
            answer[i] = list(sorted(answer[i]))
        return answer
