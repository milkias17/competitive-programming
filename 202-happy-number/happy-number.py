class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        holder = set()
        while True:
            res = 0
            for char in num:
                res += int(char) ** 2
            if res == 1:
                return True
            if res in holder:
                return False
            holder.add(res)
            num = str(res)