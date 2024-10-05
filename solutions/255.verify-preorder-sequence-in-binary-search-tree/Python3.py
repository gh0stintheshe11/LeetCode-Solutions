class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = float('-inf')
        
        for value in preorder:
            if value < low:
                return False
            while stack and value > stack[-1]:
                low = stack.pop()
            stack.append(value)
        
        return True