class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter
        
        t = []
        result = []
        count = Counter(s)
        
        min_char = min(s)
        
        for char in s:
            t.append(char)
            count[char] -= 1
            if count[char] == 0:
                del count[char]
            
            while t and (not count or t[-1] <= min(count.keys())):
                result.append(t.pop())
        
        return ''.join(result)