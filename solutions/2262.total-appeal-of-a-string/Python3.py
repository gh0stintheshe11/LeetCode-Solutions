class Solution:
    def appealSum(self, s: str) -> int:
        last_position = {}
        total_appeal = 0
        current_appeal = 0
        
        for i, char in enumerate(s):
            if char in last_position:
                current_appeal += i - last_position[char]
            else:
                current_appeal += i + 1
            
            last_position[char] = i
            total_appeal += current_appeal
        
        return total_appeal