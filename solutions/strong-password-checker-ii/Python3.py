class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        special_chars = "!@#$%^&*()-+"
        
        prev_char = ''
        
        for char in password:
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True
            if char in special_chars:
                has_special = True
            if char == prev_char:
                return False
            
            prev_char = char
        
        return has_lower and has_upper and has_digit and has_special