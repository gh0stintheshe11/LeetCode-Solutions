class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        # Calculate max value by remapping first non-9 digit to 9
        max_remap_digit = None
        for digit in num_str:
            if digit != '9':
                max_remap_digit = digit
                break
        if max_remap_digit:
            max_value = int(num_str.replace(max_remap_digit, '9'))
        else:
            max_value = num

        # Calculate min value by remapping first digit to 0
        min_remap_digit = num_str[0]
        min_value = int(num_str.replace(min_remap_digit, '0'))

        return max_value - min_value