class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = 0
        els = Counter(changed)
        res = []

        for num in sorted(changed):
            if num not in els:
                continue

            if num == 0:
                els[num] -= 1
                if els[num] >= 1:
                    res.append(num)
                els[num] -= 1
                if els[num] <= 0:
                    del els[num]
            elif num * 2 in els:
                res.append(num)
                els[num] -= 1
                if els[num] <= 0:
                    del els[num]
                els[num * 2] -= 1
                if els[num * 2] <= 0:
                    del els[num * 2]
        if len(res) * 2 != len(changed):
            return []
        
        return res