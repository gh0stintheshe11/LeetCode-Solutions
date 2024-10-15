class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If there are still digits to remove, remove them from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'