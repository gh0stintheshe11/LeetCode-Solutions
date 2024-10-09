from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages_sets = [set(lang) for lang in languages]

        # Determine non-communicating pairs
        non_communicating_pairs = []
        for u, v in friendships:
            u -= 1
            v -= 1
            if not languages_sets[u].intersection(languages_sets[v]):
                non_communicating_pairs.append((u, v))

        if not non_communicating_pairs:
            return 0

        # Find which language to teach to minimize the number of teachings
        best_teach = float('inf')
        
        for lang in range(1, n + 1):
            to_teach = set()
            for u, v in non_communicating_pairs:
                if lang not in languages_sets[u]:
                    to_teach.add(u)
                if lang not in languages_sets[v]:
                    to_teach.add(v)
            best_teach = min(best_teach, len(to_teach))
        
        return best_teach