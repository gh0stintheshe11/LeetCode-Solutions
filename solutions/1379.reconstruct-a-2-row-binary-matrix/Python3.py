from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        upper_row = [0] * n
        lower_row = [0] * n
        
        if sum(colsum) != upper + lower:
            return []
        
        for i in range(n):
            if colsum[i] == 2:
                if upper > 0 and lower > 0:
                    upper_row[i] = 1
                    lower_row[i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []
        
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    upper_row[i] = 1
                    upper -= 1
                elif lower > 0:
                    lower_row[i] = 1
                    lower -= 1
                else:
                    return []
        
        if upper == 0 and lower == 0:
            return [upper_row, lower_row]
        else:
            return []