from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        
        side_len = total_len // 4
        
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side_len
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_len:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False
        
        return backtrack(0)