class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.Node()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = self.Node()
            cur = cur.children[char]
        cur.is_word = True
    
    def _search(self, word, i, cur):
        if i == len(word) - 1:
            if word[i] == ".":
                return len(cur.children) >= 1 and any(child.is_word for child in cur.children.values())

            return word[i] in cur.children and cur.children[word[i]].is_word

        if word[i] != "." and word[i] not in cur.children:
            return False
        
        if word[i] != ".":
            return self._search(word, i + 1, cur.children[word[i]])
        
        for k in cur.children:
            if self._search(word, i + 1, cur.children[k]):
                return True
        
        return False

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)