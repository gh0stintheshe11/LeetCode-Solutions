class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # Use all "AB" pairs as they don't contribute to "AAA" or "BBB"
        # Every "AB" contributes 2 to the length
        max_size = 2 * z
        
        # Balance one "AA" and one "BB" for maximum concatenation
        # They contribute 4 for each balanced pair
        max_size += 4 * min(x, y)
        
        # If there is more "AA" or "BB", we can add an extra
        if x > y:
            max_size += 2
        elif y > x:
            max_size += 2
        
        return max_size