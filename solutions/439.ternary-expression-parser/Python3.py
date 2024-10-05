class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        
        for c in reversed(expression):
            if stack and stack[-1] == '?':
                stack.pop()  # pop '?'
                true_expr = stack.pop()
                stack.pop()  # pop ':'
                false_expr = stack.pop()
                
                if c == 'T':
                    stack.append(true_expr)
                else:
                    stack.append(false_expr)
            else:
                stack.append(c)
        
        return stack[0]