class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        def calculate_frequency(s):
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            return freq
        
        fa = calculate_frequency(a)
        fb = calculate_frequency(b)
        
        la, lb = len(a), len(b)
        
        condition3 = la + lb - max(fa[i] + fb[i] for i in range(26))
        
        # Calculate prefix sums
        fap = [0] * 26
        fbp = [0] * 26
        for i in range(26):
            fap[i] = fa[i] + (fap[i - 1] if i > 0 else 0)
            fbp[i] = fb[i] + (fbp[i - 1] if i > 0 else 0)
        
        # Find min number of changes for condition1 and condition2
        condition1 = float('inf')
        condition2 = float('inf')
        for i in range(25):
            # a < b
            condition1 = min(condition1, la - fap[i] + fbp[i])
            # b < a
            condition2 = min(condition2, lb - fbp[i] + fap[i])
        
        return min(condition1, condition2, condition3)