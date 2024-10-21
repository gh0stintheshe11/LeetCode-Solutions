from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        count = Counter(answers)
        total_rabbits = 0
        for answer, num in count.items():
            groups = (num + answer) // (answer + 1)
            total_rabbits += groups * (answer + 1)
        return total_rabbits