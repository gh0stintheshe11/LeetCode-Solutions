class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calculate_cost(digits):
            cost = 0
            current_pos = startAt
            for d in digits:
                if d != current_pos:
                    cost += moveCost
                    current_pos = d
                cost += pushCost
            return cost

        min_cost = float('inf')
        
        seconds_per_minute = 60
        max_minutes = 99
        max_seconds = 99

        for minutes in range(max_minutes + 1):
            seconds = targetSeconds - minutes * seconds_per_minute
            if 0 <= seconds <= max_seconds:
                minutes_string = str(minutes).zfill(2)
                seconds_string = str(seconds).zfill(2)
                time_string = minutes_string + seconds_string

                digits = [int(d) for d in time_string.lstrip('0')] or [0]  # Include leading zeroes

                cost = calculate_cost(digits)
                min_cost = min(min_cost, cost)

        return min_cost