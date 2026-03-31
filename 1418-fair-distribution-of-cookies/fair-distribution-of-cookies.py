class Solution:
    def backtrack(self, cookies, i, children):
        if i >= len(cookies):
            self.min_val = min(self.min_val, max(children))
            return
        
        if max(children) > self.min_val:
            return
        
        for j, child in enumerate(children):
            children[j] += cookies[i]
            self.backtrack(cookies, i + 1, children)
            children[j] -= cookies[i]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0 for _ in range(k)]
        
        self.min_val = float("inf")
        self.backtrack(cookies, 0, children)

        return self.min_val
