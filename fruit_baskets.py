from typing import List

"""
    You are visiting a farm that has a single row of fruit trees arranged
    from left to right. The trees are represented by an integer array fruits
    where fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has
    some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type
    of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit
    from every tree (including the start tree) while moving to the right. The
    picked fruits must fit in one of your baskets.  Once you reach a tree
    with fruit that cannot fit in your baskets, you must stop.  Given the
    integer array fruits, return the maximum number of fruits you can pick.


    Example 1:
    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.

    Example 2:
    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].

    Example 3:
    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].

    Constraints:
    1 <= fruits.length <= 105
    0 <= fruits[i] < fruits.length

"""


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


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([1, 2, 1]))
    print(sol.totalFruit([0, 1, 2, 2]))
    print(sol.totalFruit([1, 2, 3, 2, 2]))
    print(sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
