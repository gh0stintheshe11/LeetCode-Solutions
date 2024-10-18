class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert the string `s` into a number by replacing each letter with its position in the alphabet
        converted_number = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Convert the resulting number into a number by summing its digits repeatedly `k` times
        current_sum = sum(int(char) for char in converted_number)
        
        for _ in range(k - 1):
            current_sum = sum(int(char) for char in str(current_sum))
        
        return current_sum