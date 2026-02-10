class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)

        for num, count in counter.items():
            if len(heap) < k:
                heappush(heap, (counter[num], num))
            elif heap[0][0] < counter[num]:
                heappop(heap)
                heappush(heap, (counter[num], num))
        
        return [val[1] for val in heap]