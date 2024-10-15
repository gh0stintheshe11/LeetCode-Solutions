class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        if len(letters) >= len(digits):
            longer, shorter = letters, digits
        else:
            longer, shorter = digits, letters
        
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(longer.pop())
            else:
                result.append(shorter.pop())
                
        return ''.join(result)