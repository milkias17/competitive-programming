from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        count = 0
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                k -= 1
                count = 0

            while k == 0:
                k += nums[i] % 2
                count += 1
                i += 1

            res += count

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
