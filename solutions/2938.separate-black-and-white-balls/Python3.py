class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        zero_count = 0
        for char in reversed(s):
            if char == '0':
                zero_count += 1
            else:
                steps += zero_count
        return steps