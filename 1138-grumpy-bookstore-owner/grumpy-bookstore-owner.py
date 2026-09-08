class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_saves = 0
        saves = 0
        total = 0

        left = 0

        for right in range(len(grumpy)):
            if grumpy[right] == 0:
                total += customers[right]
            else:
                saves += customers[right]
            
            if right - left + 1 < minutes:
                continue
            
            max_saves = max(max_saves, saves)
            if grumpy[left] == 1:
                saves -= customers[left]
            left += 1
        
        return total + max_saves

            

