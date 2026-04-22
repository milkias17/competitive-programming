class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            can = False
            for need in dictionary:
                count = 0
                for i, char in enumerate(need):
                    if query[i] != char:
                        count += 1
                if count <= 2:
                    can = True
                    break
            
            if can:
                res.append(query)
                
        return res
