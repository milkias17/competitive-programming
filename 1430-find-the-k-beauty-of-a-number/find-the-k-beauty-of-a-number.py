class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        left = 0
        count = 0
        
        for right in range(0, len(num_str)):
            if right - left + 1 == k:
                cur_num = int(num_str[left:right + 1])
                if cur_num > 0 and num % cur_num == 0:
                    count += 1
                left += 1
        
        return count
