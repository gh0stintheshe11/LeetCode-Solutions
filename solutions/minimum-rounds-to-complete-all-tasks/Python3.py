from collections import Counter
from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = Counter(tasks)
        total_rounds = 0
        
        for count in task_count.values():
            if count == 1:
                return -1
            # Calculate minimum number of rounds
            rounds_for_count = count // 3
            if count % 3 != 0:
                rounds_for_count += 1
            total_rounds += rounds_for_count
        
        return total_rounds