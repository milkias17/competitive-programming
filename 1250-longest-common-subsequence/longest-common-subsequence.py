class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        nxt = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            cur = [-1] * (len(text2) + 1)
            cur[len(text2)] = 0

            for j in range(len(text2) - 1, -1, -1):
                res = 0
                if text1[i] == text2[j]:
                    res = 1 + nxt[j + 1]
                else:
                    res = max(nxt[j], cur[j + 1])
                cur[j] = res
            nxt = cur
        
        return nxt[0]