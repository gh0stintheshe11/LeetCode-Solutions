class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i].isdigit():
                # Find the first non-digit character to the left
                for j in range(i - 1, -1, -1):
                    if s[j] != '':
                        s[j] = ''  # Clear this letter
                        break
                s[i] = ''  # Clear this digit
                
        return ''.join([ch for ch in s if ch != ''])