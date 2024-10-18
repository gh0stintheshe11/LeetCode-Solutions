class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: remove excess closing brackets
        open_stack = []
        s = list(s)
        
        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == ')':
                if open_stack:
                    open_stack.pop()
                else:
                    s[i] = ''
        
        # Second pass: remove excess opening brackets
        while open_stack:
            s[open_stack.pop()] = ''
        
        return ''.join(s)