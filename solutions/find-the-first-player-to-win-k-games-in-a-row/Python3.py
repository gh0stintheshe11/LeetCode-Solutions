from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        
        if k >= n:  # If k is more than or equal to number of players.
            return skills.index(max(skills))
        
        max_skill_wins = 0
        current = skills[0]
        max_skill_index = 0
        
        for i in range(1, n):
            if skills[i] > current:
                current = skills[i]
                max_skill_wins = 1
            else:
                max_skill_wins += 1
            
            if max_skill_wins == k:
                return skills.index(current)
        
        return skills.index(current)