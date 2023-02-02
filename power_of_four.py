class Solution:
    def recurse_power_four(self, n: int, cur_index: int):
        cur_num = pow(4, cur_index)
        if cur_num == n:
            return True
        if cur_num > n:
            return False

        return self.recurse_power_four(n, cur_index + 1)

    def isPowerOfFour(self, n: int) -> bool:
        return self.recurse_power_four(n, 0)
