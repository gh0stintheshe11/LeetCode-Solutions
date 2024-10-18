class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = ""
        for i in range(len(number)):
            if number[i] == digit:
                # Form the number by removing the current digit
                current_result = number[:i] + number[i+1:]
                # Update the result to be the maximum possible
                if current_result > max_result:
                    max_result = current_result
        return max_result