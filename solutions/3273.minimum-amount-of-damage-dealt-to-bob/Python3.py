import math

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        
        n = len(damage)
        time_taken = [math.ceil(h / power) for h in health]
        dps = [(i, damage[i] / time_taken[i]) for i in range(n)]
        dps.sort(key = lambda x : x[1], reverse = True)

        total = time = 0
        for i, _ in dps:
            time += time_taken[i]
            total += time * damage[i]
        
        return total