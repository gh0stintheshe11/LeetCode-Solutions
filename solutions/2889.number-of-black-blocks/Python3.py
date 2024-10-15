class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        block_count = defaultdict(int)
        
        for x, y in coordinates:
            for dx in range(2):
                for dy in range(2):
                    if 0 <= x - dx < m - 1 and 0 <= y - dy < n - 1:
                        block_count[(x - dx, y - dy)] += 1
        
        result = [0] * 5
        for count in block_count.values():
            if 1 <= count <= 4:
                result[count] += 1

        total_blocks = (m - 1) * (n - 1)
        result[0] = total_blocks - sum(result[1:])
        
        return result