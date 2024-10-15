class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        open_count, close_count = 0, 0
        # Left to right: Check if we can balance ')' with '(' as we move
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                close_count += 1
            if close_count > open_count:
                return False
        
        open_count, close_count = 0, 0
        # Right to left: Check if we can balance '(' with ')' as we move
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                open_count += 1
            if open_count > close_count:
                return False
        
        return True