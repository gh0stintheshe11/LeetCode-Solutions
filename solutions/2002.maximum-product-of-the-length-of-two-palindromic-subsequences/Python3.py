class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindromic(bits, s):
            sub = [s[i] for i in range(len(s)) if (bits & (1 << i))]
            return sub == sub[::-1]
        
        n = len(s)
        max_product = 0
        
        # Iterate over all possible submasks
        for mask1 in range(1, 1 << n):
            if not is_palindromic(mask1, s): continue
            len1 = bin(mask1).count('1')
            
            # Iterate over all possible submasks disjoint with mask1
            for mask2 in range(1, 1 << n):
                if mask1 & mask2 == 0 and is_palindromic(mask2, s):
                    len2 = bin(mask2).count('1')
                    max_product = max(max_product, len1 * len2)
        
        return max_product