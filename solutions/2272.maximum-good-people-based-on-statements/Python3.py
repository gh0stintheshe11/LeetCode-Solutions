from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        
        def is_valid(mask):
            for i in range(n):
                if not (mask & (1 << i)):  # skip if i is not good
                    continue
                for j in range(n):
                    if statements[i][j] == 2:  # no statement about j
                        continue
                    if statements[i][j] == 1 and not (mask & (1 << j)):  # i says j is good but j is not
                        return False
                    if statements[i][j] == 0 and (mask & (1 << j)):  # i says j is bad but j is good
                        return False
            return True
        
        max_good = 0
        for mask in range(1 << n):  # try every combination
            if is_valid(mask):
                max_good = max(max_good, bin(mask).count('1'))
        
        return max_good