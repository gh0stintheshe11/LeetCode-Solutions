class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = []
        available_digits = list(range(1, n + 2))
        stack = []
        
        for i, char in enumerate(pattern):
            if char == 'I':
                stack.append(available_digits.pop(0))
                while stack:
                    result.append(stack.pop())
            elif char == 'D':
                stack.append(available_digits.pop(0))
                
        stack.append(available_digits.pop(0))
        while stack:
            result.append(stack.pop())
        
        return ''.join(map(str, result))