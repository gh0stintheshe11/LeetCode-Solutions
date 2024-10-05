from typing import List

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        result = []
        
        if low == 0:
            result.append(0)
        
        queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        while queue:
            num = queue.pop(0)
            if low <= num <= high:
                result.append(num)
            if num < high:
                last_digit = num % 10
                if last_digit > 0:
                    next_num = num * 10 + (last_digit - 1)
                    if next_num <= high:
                        queue.append(next_num)
                if last_digit < 9:
                    next_num = num * 10 + (last_digit + 1)
                    if next_num <= high:
                        queue.append(next_num)
                        
        return sorted(result)