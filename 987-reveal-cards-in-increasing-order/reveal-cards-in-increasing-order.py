class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        answer = [None] * len(deck)
        answer[0] = deck[0]
        
        queue = [i for i in range(len(answer))]
        cur = 0
        while len(queue) > 0:
            tmp = queue.pop(0)
            if answer[tmp] == None: 
                answer[tmp] = deck[cur]
                cur += 1
            else:
                cur += 1 
            
            if len(queue) == 0:
                break
            
            tmp = queue.pop(0)
            queue.append(tmp)
        
        return answer

