class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        sum_length = 0
        for word in words:
            tmp = chars_counter.copy()
            flag = True
            for char in word:
                if char not in tmp or tmp[char] <= 0:
                    flag = False
                    break
                tmp[char] -= 1
            
            if flag:
                sum_length += len(word)
        
        return sum_length
