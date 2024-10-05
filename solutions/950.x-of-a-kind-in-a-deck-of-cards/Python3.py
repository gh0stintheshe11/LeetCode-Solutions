class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        from functools import reduce
        
        count = Counter(deck).values()
        return reduce(gcd, count) >= 2