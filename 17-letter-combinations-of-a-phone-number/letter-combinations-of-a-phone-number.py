class Solution:
    def backtrack(self, digits, i, cur_set, power_set):
        if i >= len(digits):
            power_set.add("".join(cur_set))
            return
        
        for v in self.reps[digits[i]]:
            cur_set.append(v)
            self.backtrack(digits, i + 1, cur_set, power_set)
            cur_set.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.reps = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        power_set = set()
        self.backtrack(digits, 0, [], power_set)
        return list(power_set)