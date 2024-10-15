class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_chemistry = 0
        expected_skill = skill[0] + skill[-1]
        
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != expected_skill:
                return -1
            total_chemistry += skill[i] * skill[n - i - 1]
        
        return total_chemistry