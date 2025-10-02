class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        print(counter)
        return sorted(counter, key=lambda a: counter[a], reverse=True)[:k]