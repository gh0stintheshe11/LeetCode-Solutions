class Solution:
    def replaceDigits(self, s: str) -> str:
        result = []
        
        for i in range(0, len(s), 2):
            letter = s[i]
            result.append(letter)
            if i + 1 < len(s):
                digit = int(s[i + 1])
                result.append(chr(ord(letter) + digit))
        
        return ''.join(result)