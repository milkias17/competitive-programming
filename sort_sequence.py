class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split(" ")
        sentence.sort(key=lambda x: x[-1])
        sentence = " ".join(list(map(lambda x: x[:-1], sentence)))
        return sentence
