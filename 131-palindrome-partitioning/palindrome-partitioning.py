class Solution:
    def _is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def backtrack(self, s, cur, res, i):
        if i >= len(s):
            for path in cur:
                if not self._is_palindrome(path):
                    return
            res.append(cur.copy())
            return
        
        cur.append(s[i])
        self.backtrack(s, cur, res, i + 1)
        cur.pop()
        tmp = cur[-1]
        new_end = cur[-1] + s[i]
        cur[-1] = new_end
        self.backtrack(s, cur, res, i + 1)
        cur[-1] = tmp

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(s, [s[0]], res, 1)
        return res
