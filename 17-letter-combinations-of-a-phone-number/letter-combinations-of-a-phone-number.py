class Solution:
    def backtrack(self, digits: str, mapper: Dict[int, List[str]], i: int, cur: List[str], result: List[str]):
        if i > len(digits):
            return
        
        for j in mapper[digits[i]]:
            cur.append(j)
            if len(cur) == len(digits):
                result.append("".join(cur))
                cur.pop()
                continue

            self.backtrack(digits, mapper, i + 1, cur, result)
            cur.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        result = []
        self.backtrack(digits, mapper, 0, [], result)
        return result