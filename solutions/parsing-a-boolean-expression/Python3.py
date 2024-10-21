class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(expr):
            stack = []
            for char in expr:
                if char == ',':
                    continue
                elif char != ')':
                    stack.append(char)
                else:
                    sub_expr = []
                    while stack[-1] != '(':
                        sub_expr.append(stack.pop())
                    stack.pop()  # Remove '('
                    operator = stack.pop()
                    
                    if operator == '!':
                        result = not (sub_expr[0] == 't')
                    elif operator == '&':
                        result = all(sub == 't' for sub in sub_expr)
                    elif operator == '|':
                        result = any(sub == 't' for sub in sub_expr)
                    
                    stack.append('t' if result else 'f')
            
            return stack[-1] == 't'
        
        return evaluate(expression)