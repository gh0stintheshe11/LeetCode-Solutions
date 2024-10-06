class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Start from the least significant bit and move towards the most significant bit
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':  # current bit is 1
                # If carry is 0, we need to add 1 to make it even which means an extra carry
                # If carry is 1, it's already even, just reduce
                steps += 2 if carry == 0 else 1
                carry = 1  # Always have carry for odd bits
            else:  # current bit is 0
                # If carry is already 1, it's actually '10', thus one operation to become '1'
                steps += 1 if carry == 0 else 2
        
        # If there is still a carry at the end, we need an extra step to account for the final carry
        return steps + carry