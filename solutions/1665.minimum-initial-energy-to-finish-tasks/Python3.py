class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        total_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                total_energy += minimum - current_energy
                current_energy = minimum
            current_energy -= actual
        
        return total_energy