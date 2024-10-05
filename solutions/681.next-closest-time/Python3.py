import itertools

class Solution:
    def nextClosestTime(self, time: str) -> str:
        current_minutes = int(time[:2]) * 60 + int(time[3:])
        allowed_digits = {int(d) for d in time if d != ':'}
        
        while True:
            current_minutes = (current_minutes + 1) % (24 * 60)
            next_time = f"{current_minutes // 60:02}:{current_minutes % 60:02}"
            if all(int(d) in allowed_digits for d in next_time if d != ':'):
                return next_time