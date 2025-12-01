class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix_left = [cardPoints[0]]
        for i in range(1, len(cardPoints)):
            prefix_left.append(prefix_left[i - 1] + cardPoints[i])
        
        prefix_right = [0] * len(cardPoints)
        prefix_right[-1] = cardPoints[-1]
        for i in range(len(cardPoints) - 2, -1, -1):
            prefix_right[i] = prefix_right[i + 1] + cardPoints[i]
        
        count = 0
        left = 0
        right = len(cardPoints) - 1
        score = 0
        while count < k and left <= right:
            left_index = left + (k - count) - 1
            if left_index >= len(prefix_left):
                left_index = len(prefix_left) - 1

            left_val = prefix_left[left_index]
            if left != 0:
                left_val -= prefix_left[left - 1]

            right_index = right - (k - count) + 1
            if right_index < 0:
                right_index = 0
            right_val = prefix_right[right_index]
            if right != len(cardPoints) - 1:
                right_val -= prefix_right[right + 1]
            if left_val >= right_val:
                score += cardPoints[left]
                left += 1
            else:
                score += cardPoints[right]
                right -= 1
            count += 1
        
        return score