class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        red_adj = {i: [] for i in range(n)}
        blue_adj = {i: [] for i in range(n)}

        for start, end in redEdges:
            red_adj[start].append(end)

        for start, end in blueEdges:
            blue_adj[start].append(end)

        res = [-1] * n
        queue = deque()
        queue.append((0, "r", 0))
        queue.append((0, "b", 0))
        visited = set([(0, "r"), (0, "b")])

        while queue:
            cur, color, length = queue.popleft()
            if res[cur] == -1:
                res[cur] = length

            if color == "r":
                for neigh in blue_adj[cur]:
                    state = (neigh, "b", length + 1)
                    if state[:2] in visited:
                        continue

                    queue.append(state)
                    visited.add(state[:2])
            else:
                for neigh in red_adj[cur]:
                    state = (neigh, "r", length + 1)
                    if state[:2] in visited:
                        continue
                    queue.append(state)
                    visited.add(state[:2])

        return res