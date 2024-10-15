class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def countValidSubstrings(s, k):
            n = len(s)
            result = 0
            
            for start in range(n):
                count0 = 0
                count1 = 0
                for end in range(start, n):
                    if s[end] == '0':
                        count0 += 1
                    else:
                        count1 += 1
                    
                    if count0 <= k or count1 <= k:
                        result += 1
                    else:
                        break
            
            return result
        
        return countValidSubstrings(s, k)