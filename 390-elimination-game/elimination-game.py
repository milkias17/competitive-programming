class Solution:
    def helper(self, n, start=1, step=1, front=True):
        if n == 1:
            return start        

        adder = 0
        if front:
            adder = step
        elif n % 2 != 0:
            adder = step

        return self.helper(n // 2, start + adder, step * 2, not front)

    def lastRemaining(self, n: int) -> int:
        return self.helper(n)