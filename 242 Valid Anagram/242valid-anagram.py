class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counter_s = {}
        for char in s:
            counter_s[char] = counter_s.get(char, 0) + 1
        
        counter_t = {}
        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1

        for key, val in counter_t.items():
            if key not in counter_s:
                return False
            if counter_s[key] != val:
                return False
        
        return True