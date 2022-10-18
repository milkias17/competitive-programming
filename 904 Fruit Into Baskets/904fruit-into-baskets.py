class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_left = 0
        window_right = 0
        max_trees = 0
        fruit_types = {}

        while window_right < len(fruits):
            if len(fruit_types) == 2 and fruits[window_right] not in fruit_types:
                max_trees = max(max_trees, window_right - window_left)
                fruit_types[fruits[window_left]] -= 1
                if fruit_types[fruits[window_left]] == 0:
                    fruit_types.pop(fruits[window_left])
                window_left += 1
            else:
                if fruits[window_right] not in fruit_types:
                    fruit_types[fruits[window_right]] = 1
                else:
                    fruit_types[fruits[window_right]] += 1
                window_right += 1

        max_trees = max(max_trees, window_right - window_left)
        return max_trees