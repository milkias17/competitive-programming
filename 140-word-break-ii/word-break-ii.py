class Solution:
    def backtrack(self, s, words, i, cur, curset, powerset):
        if i >= len(s):
            if curset and not cur:
                powerset.append(" ".join(curset))
            return
        
        cur.append(s[i])
        cur_str = "".join(cur)
        if cur_str not in words:
            self.backtrack(s, words, i + 1, cur, curset, powerset)
            return
        
        curset.append(cur_str)
        self.backtrack(s, words, i + 1, [], curset, powerset)
        curset.pop()
        self.backtrack(s, words, i + 1, cur, curset, powerset)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        powerset = []
        self.backtrack(s, set(wordDict), 0, [], [], powerset)
        return powerset