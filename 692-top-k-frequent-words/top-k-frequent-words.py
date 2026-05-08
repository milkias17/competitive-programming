class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [(-count, word) for word, count in counter.items()]
        heapify(heap)

        res = []
        while len(res) < k:
            count, word = heappop(heap)
            res.append(word)
        
        return res
