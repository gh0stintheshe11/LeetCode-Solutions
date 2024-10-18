class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def evaluate_correct(expr):
            # For evaluating correct expression as per precedence: * first then +
            operand_stack, operator = [], []
            current_num = 0
            
            for char in expr + "+":
                if char.isdigit():
                    current_num = current_num * 10 + int(char)
                else:
                    if operator and operator[-1] == '*':
                        operand_stack[-1] *= current_num
                        operator.pop()
                    else:
                        operand_stack.append(current_num)
                    current_num = 0
                    operator.append(char)
            
            result = operand_stack[0]
            for i in range(1, len(operand_stack)):
                result += operand_stack[i]
            return result
        
        def evaluate_dummy(expr, l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            
            if l == r:
                return {int(expr[l])}
            
            result_set = set()
            for k in range(l + 1, r, 2):
                left_results = evaluate_dummy(expr, l, k - 1)
                right_results = evaluate_dummy(expr, k + 1, r)
                op = expr[k]
                
                for lv in left_results:
                    for rv in right_results:
                        if op == '+':
                            value = lv + rv
                        elif op == '*':
                            value = lv * rv
                        if value <= 1000:
                            result_set.add(value)
            
            memo[(l, r)] = result_set
            return result_set
        
        correct_answer = evaluate_correct(s)
        memo = {}
        possible_wrong_answers = evaluate_dummy(s, 0, len(s) - 1)
        
        total_score = 0
        
        for ans in answers:
            if ans == correct_answer:
                total_score += 5
            elif ans in possible_wrong_answers:
                total_score += 2
        
        return total_score