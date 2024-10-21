from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        def count_ones(dx: int, dy: int) -> int:
            count = 0
            for x in range(n):
                for y in range(n):
                    if 0 <= x + dx < n and 0 <= y + dy < n:
                        count += img1[x][y] * img2[x + dx][y + dy]
            return count

        max_overlap = 0
        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):
                max_overlap = max(max_overlap, count_ones(dx, dy))
        
        return max_overlap