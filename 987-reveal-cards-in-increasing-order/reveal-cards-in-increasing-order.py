class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        answer = []
        i = 0
        while len(answer) < len(deck):
            answer.append(sorted_deck[i])
            if len(answer) < len(deck):
                answer.append(None)
            i += 1
        
        queue = [i for i in range(len(answer))]
        cur = 0
        while len(queue) > 0:
            tmp = queue.pop(0)
            if answer[tmp] == None: 
                answer[tmp] = sorted_deck[cur]
                cur += 1
            else:
                cur += 1 
            
            if len(queue) == 0:
                break
            
            tmp = queue.pop(0)
            queue.append(tmp)
        
        return answer

