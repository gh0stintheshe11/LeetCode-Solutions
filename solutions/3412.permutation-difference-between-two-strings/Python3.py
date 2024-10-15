class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index_map_s = {char: idx for idx, char in enumerate(s)}
        index_map_t = {char: idx for idx, char in enumerate(t)}
        
        difference = 0
        for char in s:
            difference += abs(index_map_s[char] - index_map_t[char])
        
        return difference