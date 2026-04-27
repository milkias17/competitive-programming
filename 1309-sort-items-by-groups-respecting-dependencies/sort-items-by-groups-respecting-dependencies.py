class Solution:
    def top_sort(self, items, adj, in_degree):
        queue = deque([item for item in items if in_degree[item] == 0])
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for neigh in adj[cur]:
                in_degree[neigh] -= 1
                if in_degree[neigh] <= 0:
                    queue.append(neigh)

        # print(f"Res: {res}")
        return res if len(res) == len(items) else []

    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1

        adj_group = {i: set() for i in range(m)}
        in_degree_group = {i: 0 for i in range(m)}

        for i, prereq in enumerate(beforeItems):
            count = 0
            for item in prereq:
                adj[item].append(i)
                if group[item] != group[i] and group[i] not in adj_group[group[item]]:
                    adj_group[group[item]].add(group[i])
                    count += 1

            in_degree[i] += len(prereq)
            in_degree_group[group[i]] += count

        group_order = self.top_sort(in_degree_group.keys(), adj_group, in_degree_group)
        items_order = self.top_sort(in_degree.keys(), adj, in_degree)

        if not group_order or not items_order:
            return []

        group_mapper = defaultdict(list)

        for item in items_order:
            group_mapper[group[item]].append(item)

        res = []
        for grp in group_order:
            res.extend(group_mapper[grp])

        return res