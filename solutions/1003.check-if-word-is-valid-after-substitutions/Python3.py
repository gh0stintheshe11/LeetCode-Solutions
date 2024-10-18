class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack