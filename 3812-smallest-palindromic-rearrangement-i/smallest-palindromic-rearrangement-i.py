class Solution:
    def smallestPalindrome(self, s: str) -> str:
        splitted = list(s)
        splitted.sort()
        new_str = [None] * len(splitted)
        left = 0
        right = len(new_str) - 1

        i = 0
        store = None
        while i < len(splitted):
            if i + 1 < len(splitted) and splitted[i + 1] == splitted[i]:
                new_str[left] = splitted[i]
                new_str[right] = splitted[i]
                left += 1
                right -= 1
                i += 2
            else:
                store = splitted[i]
                i += 1

        if store is not None:
            new_str[len(new_str) // 2] = store
        return "".join(new_str)