class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []
        heights = []
        max_height = 0
        
        for left, size in positions:
            right = left + size
            base_height = 0
            
            for (l, r, h) in intervals:
                if l < right and left < r:  # overlapping intervals
                    base_height = max(base_height, h)
            
            current_height = base_height + size
            intervals.append((left, right, current_height))
            max_height = max(max_height, current_height)
            heights.append(max_height)
        
        return heights