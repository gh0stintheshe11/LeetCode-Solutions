class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step, sum_steps = 0, 0
        
        while sum_steps < target or (sum_steps - target) % 2 != 0:
            step += 1
            sum_steps += step
            
        return step