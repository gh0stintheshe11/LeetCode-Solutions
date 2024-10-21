class Solution:
    def minTimeToType(self, word: str) -> int:
        total_time = 0
        current_position = 'a'
        
        for char in word:
            clockwise_distance = abs(ord(char) - ord(current_position))
            counterclockwise_distance = 26 - clockwise_distance
            total_time += min(clockwise_distance, counterclockwise_distance) + 1
            current_position = char
        
        return total_time