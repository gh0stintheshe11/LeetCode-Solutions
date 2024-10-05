class Solution:
    def confusingNumber(self, n: int) -> bool:
        # Mapping of digits to their rotated counterparts
        rotate_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        
        # Convert the number to a string to easily access each digit
        str_n = str(n)
        
        # Initialize the rotated number as an empty string
        rotated_str = ""
        
        # Iterate through each digit in the original number
        for digit in str_n:
            # Convert the digit to an integer
            int_digit = int(digit)
            
            # Check if the digit is in the rotate_map
            if int_digit not in rotate_map:
                # If the digit is not valid, return False
                return False
            
            # Append the rotated counterpart to the rotated_str
            rotated_str = str(rotate_map[int_digit]) + rotated_str
        
        # Convert the rotated string back to an integer
        rotated_number = int(rotated_str)
        
        # Check if the rotated number is different from the original number
        return rotated_number != n