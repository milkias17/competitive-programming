class UnionFind:
    def __init__(self):
        self.email_name = {}
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        
        return root
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True

    def add(self, account):
        chosen = account[1]
        self.email_name[chosen] = account[0]
        if chosen not in self.parent:
            self.parent[chosen] = chosen
            self.rank[chosen] = 0
        
        for email in account[2:]:
            self.email_name[email] = account[0]
            if email not in self.parent:
                self.parent[email] = email
                self.rank[email] = 0
            
            self.union(chosen, email)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        for account in accounts:
            uf.add(account)
        
        final = defaultdict(list)
        for k in uf.parent:
            final[uf.find(k)].append(k)
        
        res = []
        for k, v in final.items():
            name = uf.email_name[k]
            v.sort()
            v.insert(0, name)
            res.append(v)
        
        return res

