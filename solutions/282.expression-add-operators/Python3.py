from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            
            for i in range(index, len(num)):
                curr_str = num[index:i+1]
                curr_num = int(curr_str)
                
                if index == 0:
                    # Start of expression
                    backtrack(i+1, curr_str, curr_num, curr_num)
                else:
                    # Addition
                    backtrack(i+1, path + "+" + curr_str, value + curr_num, curr_num)
                    # Subtraction
                    backtrack(i+1, path + "-" + curr_str, value - curr_num, -curr_num)
                    # Multiplication
                    backtrack(i+1, path + "*" + curr_str, value - last + last * curr_num, last * curr_num)
                
                # Avoid numbers with leading zero
                if num[index] == '0':
                    break
        
        result = []
        backtrack(0, "", 0, 0)
        return result