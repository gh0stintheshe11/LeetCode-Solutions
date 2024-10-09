class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)
        
        for char in s:
            stack.append(char)
            # Check if the end of the stack matches `part`
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                # Remove the last `part_len` characters
                for _ in range(part_len):
                    stack.pop()
        
        return ''.join(stack)