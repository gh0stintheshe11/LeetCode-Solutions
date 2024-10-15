class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_num = -1
        tokens = s.split()

        for token in tokens:
            if token.isdigit():
                current_num = int(token)
                if current_num <= prev_num:
                    return False
                prev_num = current_num
        
        return True