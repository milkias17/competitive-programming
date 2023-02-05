from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1

        sorted_nums = sorted(counter_dict.keys(), key=lambda x: counter_dict[x], reverse=True)
        return sorted_nums[:k]


if __name__ == "__main__":
    sol = Solution()
    x = sol.topKFrequent([1, 1, 1, 1, 2, 2, 3, 4], 2)
    print(x)
