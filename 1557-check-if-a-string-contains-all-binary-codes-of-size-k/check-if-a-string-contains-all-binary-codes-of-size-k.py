import itertools

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code_perms = set(map(lambda x: "".join(x), itertools.product("01", repeat=k)))
        left = 0
        for right in range(len(s)):
            if right - left + 1 == k:
                if s[left: right + 1] in code_perms:
                    code_perms.remove(s[left: right + 1])
                left += 1
        
        return len(code_perms) == 0