class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        
        new_str = ""
        for i in range(idx, -1, -1):
            new_str += word[i]
        
        return new_str + word[idx + 1: len(word)]
