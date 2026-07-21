class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i, tmp in enumerate(edges):
            src, dest = tmp

            adj[src].append((succProb[i], dest))
            adj[dest].append((succProb[i], src))
        
        best_probs = {i: -1 for i in range(n)}
        heap = [(1, start_node)]

        while heap:
            w1, n1 = heapq.heappop_max(heap)
            if n1 == end_node:
                return w1
            
            if best_probs[n1] != -1:
                continue
            
            best_probs[n1] = w1

            for w2, n2 in adj[n1]:
                heapq.heappush_max(heap, (w2 * w1, n2))
            
        
        return 0
