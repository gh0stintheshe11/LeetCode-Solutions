class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def to_float(num: str) -> float:
            if '(' not in num:
                return float(num)
            integer_part, remainder = num.split('.')
            non_repeating_part, repeating_part = remainder.split('(')
            repeating_part = repeating_part.rstrip(')')
            base_num = integer_part + '.' + non_repeating_part
            if not repeating_part:
                return float(base_num)
            power_len = len(repeating_part)
            return float(base_num + repeating_part * 20)
        
        return to_float(s) == to_float(t)