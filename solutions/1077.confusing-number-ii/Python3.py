class Solution:
    
    def confusingNumberII(self, n: int) -> int:
        valid_digits = ['0', '1', '6', '8', '9']
        rot_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        def is_confusing(num):
            original = str(num)
            rotated = ''.join(rot_map[ch] for ch in reversed(original))
            return original != rotated and rotated.lstrip('0') != original

        def dfs(current):
            if current > n:
                return 0

            count = 0
            if current != 0 and is_confusing(current):
                count += 1

            for digit in valid_digits:
                next_num = current * 10 + int(digit)
                if next_num != 0:  # To avoid leading 0s
                    count += dfs(next_num)
                
            return count

        # Starting from each valid digit to avoid leading zeros
        total_count = 0
        for digit in valid_digits[1:]:
            total_count += dfs(int(digit))
        
        return total_count