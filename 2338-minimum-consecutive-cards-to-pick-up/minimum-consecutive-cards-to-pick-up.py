class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf")
        holder = set()
        left = 0
        for right in range(len(cards)):
            while cards[right] in holder:
                res = min(res, right - left + 1)
                holder.remove(cards[left])
                left += 1
            
            holder.add(cards[right])
            

        return res if res != float("inf") else -1