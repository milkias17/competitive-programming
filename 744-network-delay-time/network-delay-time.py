class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, target, weight in times:
            adj[src].append((weight, target))
        
        heap = [(0, k)]
        visited = set()
        total_time = float("-inf")

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            total_time = max(total_time, w1)

            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w2 + w1, n2))
        
        return total_time if len(visited)  == n else -1

