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

        def bfs(start, end):
            queue = deque()
            queue.append((start, "r", 0))
            queue.append((start, "b", 0))
            visited = set([(start, "r"), (start, "b")])

            while queue:
                cur, color, length = queue.popleft()
                if cur == end:
                    return length

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

            return -1

        res = []
        for i in range(n):
            res.append(bfs(0, i))

        return res