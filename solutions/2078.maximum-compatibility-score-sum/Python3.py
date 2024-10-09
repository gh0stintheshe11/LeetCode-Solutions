from typing import List
from itertools import permutations

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def compatibility_score(student, mentor):
            return sum(s == m for s, m in zip(student, mentor))
        
        m = len(students)
        max_score = 0
        for perm in permutations(range(m)):
            score = 0
            for i in range(m):
                score += compatibility_score(students[i], mentors[perm[i]])
            max_score = max(max_score, score)
        
        return max_score