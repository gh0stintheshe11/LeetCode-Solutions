class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_string(s: str) -> str:
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return final_string(s) == final_string(t)