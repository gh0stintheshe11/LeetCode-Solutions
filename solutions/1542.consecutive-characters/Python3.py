class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        current_power = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_power += 1
            else:
                current_power = 1
            max_power = max(max_power, current_power)
        
        return max_power