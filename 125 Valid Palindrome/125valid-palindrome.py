class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for char in s:
            if not char.isalnum():
                continue
            new_s += char.lower()
        
        left_ptr = 0
        right_ptr = len(new_s) - 1
        while left_ptr < right_ptr:
            if new_s[left_ptr] != new_s[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1
        
        return True