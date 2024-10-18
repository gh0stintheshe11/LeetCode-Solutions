from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_numbers = {f for f, b in zip(fronts, backs) if f == b}
        candidates = set(fronts + backs) - same_numbers
        return min(candidates) if candidates else 0