from typing import List
import collections

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = {v: i for v, i in zip(evalvars, evalints)}
        
        def combine(left, right, symbol):
            if symbol in '+-':
                sign = 1 if symbol == '+' else -1
                for k, v in right.items():
                    left[k] += sign * v
            elif symbol == '*':
                ans = collections.Counter()
                for k1, v1 in left.items():
                    for k2, v2 in right.items():
                        newk = tuple(sorted(k1 + k2))
                        ans[newk] += v1 * v2
                return ans
            return left
        
        def make(expr):
            if expr.isdigit():
                return collections.Counter({(): int(expr)})
            if expr in evalmap:
                return collections.Counter({(): evalmap[expr]})
            return collections.Counter({(expr,): 1})
        
        def parse(expr):
            buckets = []
            operators = []
            operand = ''
            
            def closeParentheses():
                top = buckets.pop()
                while operators[-1] != '(':
                    symbol = operators.pop()
                    top = combine(buckets.pop(), top, symbol)
                operators.pop()  # Remove '('
                buckets.append(top)
            
            def addOperand():
                nonlocal operand
                if operand:
                    buckets.append(make(operand))
                    operand = ''
            
            i = 0
            while i < len(expr):
                if expr[i] == ' ':
                    i += 1
                    continue
                if expr[i].isalnum():
                    operand += expr[i]
                else:
                    addOperand()
                    if expr[i] == '(':
                        operators.append('(')
                    elif expr[i] == ')':
                        closeParentheses()
                    elif expr[i] in '+-*':
                        while operators and operators[-1] != '(' and (operators[-1] == '*' or expr[i] in '+-'):
                            right = buckets.pop()
                            left = buckets.pop()
                            buckets.append(combine(left, right, operators.pop()))
                        operators.append(expr[i])
                i += 1
            addOperand()
            while operators:
                right = buckets.pop()
                left = buckets.pop()
                buckets.append(combine(left, right, operators.pop()))
            return buckets.pop()
        
        ans = parse(expression)
        result = [f"{v}{'*' if k else ''}{'*'.join(k)}" for k, v in sorted(ans.items(), key=lambda x: (-len(x[0]), x[0])) if v]
        
        return result