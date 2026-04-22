class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for i in range(len(nums))]

        for val, count in counter.items():
            freq[count - 1].append(val)
        
        res = []

        print(freq)
        for i in range(len(freq) - 1, -1, -1):
            res.extend(freq[i])
            if len(res) >= k:
                break
        
        return res[:k]
