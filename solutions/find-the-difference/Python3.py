class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a variable to hold the XOR result
        result = 0
        
        # XOR all characters in s
        for char in s:
            result ^= ord(char)
        
        # XOR all characters in t
        for char in t:
            result ^= ord(char)
        
        # The result will be the ASCII value of the extra character
        return chr(result)
