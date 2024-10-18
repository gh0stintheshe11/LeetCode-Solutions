class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        prefix = [0] * (n + 1)
        
        # Calculate prefix sums of white tiles
        for i in range(n):
            prefix[i + 1] = prefix[i] + (tiles[i][1] - tiles[i][0] + 1)
        
        max_covered = 0
        j = 0
        
        # Use a sliding window approach
        for i in range(n):
            start = tiles[i][0]
            end = start + carpetLen - 1
            
            # Move j forward to find the farthest end within the carpetLen from tiles[i][0]
            while j < n and tiles[j][1] < end:
                j += 1
            
            # Check the prefix and extra part
            if j < n and tiles[j][0] <= end:
                total_covered = prefix[j] - prefix[i] + (end - tiles[j][0] + 1)
            else:
                total_covered = prefix[j] - prefix[i]
            
            max_covered = max(max_covered, total_covered)
        
        return max_covered