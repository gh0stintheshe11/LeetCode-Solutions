class Solution:
    def calculate(self, s: str) -> int:
        def helper(it):
            num = 0
            stack = []
            sign = '+'
            
            while it < len(s):
                char = s[it]
                it += 1
                
                if char.isdigit():
                    num = num * 10 + int(char)
                
                if char == '(':
                    num, it = helper(it)
                
                if (not char.isdigit() and char != ' ') or it == len(s):
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                    
                    sign = char
                    num = 0
                
                if char == ')':
                    break
            
            return sum(stack), it
        
        return helper(0)[0]