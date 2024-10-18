class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        result = list(s)

        # Find the first non-'a' character
        i = 0
        while i < n and s[i] == 'a':
            i += 1
        
        if i == n:
            # All characters are 'a'
            result[-1] = 'z'
        else:
            # From the first non-'a' character, decrement until we encounter 'a' again
            while i < n and s[i] != 'a':
                result[i] = chr(ord(s[i]) - 1)
                i += 1
            
        return "".join(result)