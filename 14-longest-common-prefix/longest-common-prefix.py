class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        left = 0
        right = 1
        prefix = ""
        for i, char in enumerate(strs[1]):
            if i >= len(strs[left]):
                break

            if strs[left][i] == char:
                prefix += char
            else:
                break

        if prefix == "":
            return prefix
        
        for word in strs[right + 1:]:
            count = 0
            for i, char in enumerate(word):
                if i >= len(prefix):
                    break
                    
                if prefix[i] == char:
                    count += 1
                else:
                    break
            
            if count == 0:
                return ""
            
            prefix = prefix[:count]
        
        return prefix

