class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 != 0:
                target -= 1
                moves += 1
            
            target = target // 2
            maxDoubles -= 1
            moves += 1
        
        print(f"Moves: {moves}, target now: {target}, maxD: {maxDoubles}")
        return moves + (target - 1)