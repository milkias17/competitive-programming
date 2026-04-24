class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = Counter(moves)

        if counter["R"] > counter["L"]:
            counter["R"] += counter["_"]
        else:
            counter["L"] += counter["_"]
        
        return abs(counter["R"] - counter["L"])