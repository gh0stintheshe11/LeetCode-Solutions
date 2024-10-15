class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index = expression.index('+')
        num1, num2 = expression[:plus_index], expression[plus_index + 1:]
        min_value = float('inf')
        result_expr = ""
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                a = int(num1[:i]) if i > 0 else 1
                b = int(num1[i:]) 
                c = int(num2[:j + 1])
                d = int(num2[j + 1:]) if j + 1 < len(num2) else 1
                current_value = a * (b + c) * d
                if current_value < min_value:
                    min_value = current_value
                    result_expr = num1[:i] + '(' + num1[i:] + '+' + num2[:j + 1] + ')' + num2[j + 1:]
        
        return result_expr