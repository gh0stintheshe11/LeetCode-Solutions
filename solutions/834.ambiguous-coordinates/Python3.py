class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def generate_valid_nums(subs: str) -> List[str]:
            n = len(subs)
            if n == 0: return []
            if n == 1: return [subs]
            result = []
            if subs[0] == '0':
                if subs[-1] == '0':
                    if n == 1: result.append('0')
                else:
                    result.append('0.' + subs[1:])
            elif subs[-1] == '0':
                result.append(subs)
            else:
                result.append(subs)
                for i in range(1, n):
                    result.append(subs[:i] + '.' + subs[i:])
            return result

        s = s[1:-1]
        n = len(s)
        result = []
        
        for i in range(1, n):
            x_part = s[:i]
            y_part = s[i:]
            x_candidates = generate_valid_nums(x_part)
            y_candidates = generate_valid_nums(y_part)
            
            for x in x_candidates:
                for y in y_candidates:
                    result.append(f"({x}, {y})")
                    
        return result