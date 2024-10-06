class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = sum(1 for p in position if p % 2 == 0)
        odd_count = len(position) - even_count
        return min(even_count, odd_count)