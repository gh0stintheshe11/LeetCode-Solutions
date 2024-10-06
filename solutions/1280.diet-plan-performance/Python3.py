class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        window_sum = sum(calories[:k])
        
        if window_sum < lower:
            points -= 1
        elif window_sum > upper:
            points += 1
        
        for i in range(k, len(calories)):
            window_sum += calories[i] - calories[i - k]
            
            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1
        
        return points