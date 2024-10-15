class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1, pos2 = -1, -1
        min_distance = float('inf')
        
        for idx, word in enumerate(wordsDict):
            if word == word1:
                pos1 = idx
            elif word == word2:
                pos2 = idx
            
            if pos1 != -1 and pos2 != -1:
                min_distance = min(min_distance, abs(pos1 - pos2))
                
        return min_distance