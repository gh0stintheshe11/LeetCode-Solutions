class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        has_lower = any('a' <= c <= 'z' for c in password)
        has_upper = any('A' <= c <= 'Z' for c in password)
        has_digit = any('0' <= c <= '9' for c in password)
        
        missing_type = int(not has_lower) + int(not has_upper) + int(not has_digit)
        
        change = 0
        one = two = 0
        
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                
                change += length // 3
                
                if length % 3 == 0: 
                    one += 1
                elif length % 3 == 1: 
                    two += 1
            else:
                i += 1
        
        if n < 6:
            return max(missing_type, 6 - n)
        elif n <= 20:
            return max(missing_type, change)
        else:
            delete = n - 20
            
            change -= min(delete, one * 1) // 1
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            
            return delete + max(missing_type, change)