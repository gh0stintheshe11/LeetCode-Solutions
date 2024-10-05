class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            coef, const = 0, 0
            num, sign, i, n = 0, 1, 0, len(expr)
            while i < n:
                if expr[i] in ['+', '-']:
                    sign = 1 if expr[i] == '+' else -1
                    i += 1
                elif expr[i].isdigit():
                    num = 0
                    while i < n and expr[i].isdigit():
                        num = num * 10 + int(expr[i])
                        i += 1
                    if i < n and expr[i] == 'x':
                        coef += sign * num
                        i += 1
                    else:
                        const += sign * num
                elif expr[i] == 'x':
                    coef += sign
                    i += 1
            return coef, const
        
        left, right = equation.split('=')
        left_coef, left_const = parse(left)
        right_coef, right_const = parse(right)
        
        coef = left_coef - right_coef
        const = right_const - left_const
        
        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={const // coef}"