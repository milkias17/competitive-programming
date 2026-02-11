class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counter_2 = Counter(word2)
        counter_1 = Counter(word1)
        tmp = {}
        for k, v in counter_1.items():
            if k not in counter_2:
                return False
            tmp[v] = tmp.get(v, 0) + 1

        for k, v in counter_2.items():
            if k not in counter_1:
                return False
            if v not in tmp:
                return False
            if tmp[v] <= 0:
                return False
            tmp[v] -= 1
        
        return True

