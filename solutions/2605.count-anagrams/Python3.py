class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        from math import factorial
        from collections import Counter
        
        words = s.split()
        result = 1
        
        for word in words:
            count = Counter(word)
            anagrams_count = factorial(len(word))
            for freq in count.values():
                anagrams_count //= factorial(freq)
            result = (result * anagrams_count) % MOD
        
        return result