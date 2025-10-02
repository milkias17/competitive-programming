class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapper = {}
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word not in mapper:
                mapper[s_word] = [word]
            else:
                mapper[s_word].append(word)
        
        return mapper.values()
