class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        needed = skill[-1] + skill[0]

        for left in range(len(skill) // 2):
            right = len(skill) - 1 - left
            if skill[left] + skill[right] != needed:
                return -1
            chemistry += skill[left] * skill[right]
        
        return chemistry
