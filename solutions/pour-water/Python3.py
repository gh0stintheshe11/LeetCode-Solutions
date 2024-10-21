class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        def find_position(heights, k, direction):
            pos = k
            while 0 <= pos + direction < len(heights) and heights[pos + direction] <= heights[pos]:
                if heights[pos + direction] < heights[pos]:
                    pos += direction
                elif heights[pos + direction] == heights[pos]:
                    pos2 = pos + direction
                    while 0 <= pos2 + direction < len(heights) and heights[pos2 + direction] == heights[pos2]:
                        pos2 += direction
                    if 0 <= pos2 + direction < len(heights) and heights[pos2 + direction] < heights[pos2]:
                        pos = pos2 + direction
                    else:
                        break
            return pos
        
        for _ in range(volume):
            pos = find_position(heights, k, -1)
            if pos == k:
                pos = find_position(heights, k, 1)
            heights[pos] += 1
        
        return heights