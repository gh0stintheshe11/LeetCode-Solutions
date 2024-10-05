class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(tokens):
            stack = []
            num = 0
            sign = 1
            result = 0
            i = 0
            
            while i < len(tokens):
                char = tokens[i]
                
                if char.isdigit():
                    num = num * 10 + int(char)
                
                elif char == '+':
                    result += sign * num
                    num = 0
                    sign = 1
                    
                elif char == '-':
                    result += sign * num
                    num = 0
                    sign = -1
                
                elif char == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                
                elif char == ')':
                    result += sign * num
                    num = 0
                    result *= stack.pop()  # sign before the parenthesis
                    result += stack.pop()  # result calculated before the parenthesis
                    
                i += 1
            
            result += sign * num
            return result
        
        tokens = [ch for ch in s if ch != ' ']
        return evaluate(tokens)