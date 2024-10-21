from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # A memoization dictionary to store results of sub-expressions
        memo = {}
        
        def compute(expression: str) -> List[int]:
            # If the result for this expression is already computed, return it
            if expression in memo:
                return memo[expression]
            
            results = []
            # Iterate through the expression to find operators
            for i, char in enumerate(expression):
                if char in "+-*":
                    # Split the expression into left and right parts
                    left = compute(expression[:i])
                    right = compute(expression[i+1:])
                    
                    # Combine the results from left and right parts using the current operator
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)
            
            # If no operator is found, it means the expression is a single number
            if not results:
                results.append(int(expression))
            
            # Store the computed results in the memo dictionary
            memo[expression] = results
            return results
        
        return compute(expression)