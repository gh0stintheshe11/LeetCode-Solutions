class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        neededEnergy = sum(energy) + 1 - initialEnergy
        neededExperience = 0
        
        currentExperience = initialExperience
        for exp in experience:
            if currentExperience <= exp:
                neededExperience += exp + 1 - currentExperience
                currentExperience = exp + 1
            currentExperience += exp
        
        return max(neededEnergy, 0) + neededExperience