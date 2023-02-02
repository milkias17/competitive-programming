"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""


class Solution:
    def recurse_power_three(self, n: int, cur_index: int):
        cur_num = pow(3, cur_index)
        if cur_num == n:
            return True
        if cur_num > n:
            return False

        return self.recurse_power_three(n, cur_index + 1)

    def isPowerOfThree(self, n: int) -> bool:
        return self.recurse_power_three(n, 0)


if __name__ == "__main__":
    sol = Solution()
    sol.isPowerOfThree(3)
