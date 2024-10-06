class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        
        counter = Counter(s)
        result = []
        
        while counter:
            for char in sorted(counter):  # Step 1, 2, 3
                result.append(char)
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
            
            for char in sorted(counter, reverse=True):  # Step 4, 5, 6
                result.append(char)
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
        
        return ''.join(result)