class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # Function to perform replacement
        def replace(s, a, b):
            return s.replace(a, b)
        
        # Find the maximum possible value of a
        # Replace the first occurrence of a non-'9' digit with '9'
        for digit in num_str:
            if digit != '9':
                max_num_str = replace(num_str, digit, '9')
                break
        else:
            max_num_str = num_str
        
        # Find the minimum possible value of b
        # Replace the first digit with '1' if it is different from '1'
        # or replace the first occurrence of a non-zero and non-first digit to '0'
        if num_str[0] != '1':
            min_num_str = replace(num_str, num_str[0], '1')
        else:
            for digit in num_str[1:]:
                if digit != '0' and digit != num_str[0]:
                    min_num_str = replace(num_str, digit, '0')
                    break
            else:
                min_num_str = num_str
        
        # Convert replaced strings back to integers
        a = int(max_num_str)
        b = int(min_num_str)
        
        # Return max difference between a and b
        return a - b