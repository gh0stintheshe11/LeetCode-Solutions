class Solution:
    def countAndSay(self, n: int) -> str:
        def next_sequence(s: str) -> str:
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(f"{count}{s[i]}")
                i += 1
            return ''.join(result)
        
        current_sequence = "1"
        for _ in range(n - 1):
            current_sequence = next_sequence(current_sequence)
        
        return current_sequence