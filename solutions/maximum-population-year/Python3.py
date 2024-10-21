class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_changes = [0] * 101  # To cover years from 1950 to 2050 (exclusive 2051)
        
        for birth, death in logs:
            year_changes[birth - 1950] += 1
            year_changes[death - 1950] -= 1
        
        max_population = 0
        max_year = 1950
        current_population = 0
        
        for year in range(101):
            current_population += year_changes[year]
            if current_population > max_population:
                max_population = current_population
                max_year = 1950 + year
        
        return max_year