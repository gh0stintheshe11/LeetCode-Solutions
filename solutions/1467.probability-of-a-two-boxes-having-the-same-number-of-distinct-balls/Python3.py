from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        half_balls = total_balls // 2
        n_colors = len(balls)
        
        cache = {}
        
        def dfs(i, b1, b2, d1, d2, w1, w2):
            if i == n_colors:
                if b1 == half_balls and b2 == half_balls and d1 == d2:
                    return 1
                return 0
            
            if (i, b1, b2, d1, d2, w1, w2) in cache:
                return cache[(i, b1, b2, d1, d2, w1, w2)]
            
            total_ways = comb(w1 + w2, w1)
            valid_ways = 0
            
            for pick in range(balls[i] + 1):
                new_d1 = d1 + (1 if pick > 0 else 0)
                new_d2 = d2 + (1 if balls[i] - pick > 0 else 0)
                
                n_valid = dfs(
                    i + 1,
                    b1 + pick,
                    b2 + (balls[i] - pick),
                    new_d1,
                    new_d2,
                    w1 + pick,
                    w2 + (balls[i] - pick)
                )
                
                valid_ways += n_valid * comb(balls[i], pick)
            
            cache[(i, b1, b2, d1, d2, w1, w2)] = valid_ways
            return valid_ways
        
        valid_distribution = dfs(0, 0, 0, 0, 0, 0, 0)
        all_distribution = comb(total_balls, half_balls)
        
        return valid_distribution / all_distribution