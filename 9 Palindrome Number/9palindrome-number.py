class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        reverse_x = ""
        for i in range(len(str_x) - 1, -1, -1):
            reverse_x += str_x[i]
        
        return reverse_x == str_x