class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def dp(range_end):
            x = str(range_end)
            total = 0
            while len(x) > len(s):
                digit_count = (limit + 1)**(len(x) - len(s) - 1) 
                if int(x[0]) > limit:
                    total += (limit+1) * digit_count 
                    return total 
                total += digit_count * (min(limit, int(x[0])))
                x = x[1:]
            if int(x) < int(s):
                total -= 1
            return total + 1
        return dp(finish) - dp(start-1)