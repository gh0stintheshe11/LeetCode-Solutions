class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Memoization dictionary to store results of subproblems
        memo = {}
        
        def is_scramble_recursive(s1, s2):
            # If the result is already computed, return it
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            # If the strings are equal, they are trivially scrambled versions
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            
            # If the sorted characters of both strings do not match, they cannot be scrambled versions
            if sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            
            n = len(s1)
            for i in range(1, n):
                # Check if there is a valid split where the substrings are scrambled versions
                if (is_scramble_recursive(s1[:i], s2[:i]) and is_scramble_recursive(s1[i:], s2[i:])) or \
                   (is_scramble_recursive(s1[:i], s2[-i:]) and is_scramble_recursive(s1[i:], s2[:-i])):
                    memo[(s1, s2)] = True
                    return True
            
            # If no valid split is found, the strings are not scrambled versions
            memo[(s1, s2)] = False
            return False
        
        return is_scramble_recursive(s1, s2)