class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                current_string = []
                while stack and stack[-1] != '(':
                    current_string.append(stack.pop())
                stack.pop()  # Remove the '('
                stack.extend(current_string)
            else:
                stack.append(char)
        return ''.join(stack)