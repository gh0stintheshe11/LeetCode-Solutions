class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        equivalent_pairs = 0
        
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            equivalent_pairs += count[key]
            count[key] += 1
        
        return equivalent_pairs