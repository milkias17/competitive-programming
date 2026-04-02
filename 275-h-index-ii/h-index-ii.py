class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = 1001

        while left + 1 < right:
            mid = left + (right - left) // 2

            i_left = -1
            i_right = len(citations)

            while i_left + 1 < i_right:
                i_mid = i_left + (i_right - i_left) // 2

                if citations[i_mid] >= mid:
                    i_right = i_mid
                else:
                    i_left = i_mid
            
            if len(citations) - i_right >= mid:
                left = mid
            else:
                right = mid
        
        return left
            
