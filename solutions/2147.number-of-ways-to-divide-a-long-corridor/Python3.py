class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        # Find all indices of 'S'
        seat_indices = [i for i, ch in enumerate(corridor) if ch == 'S']

        # If the number of seats isn't a multiple of 2 or is less than 2, division isn't possible
        if len(seat_indices) % 2 != 0 or len(seat_indices) < 2:
            return 0
        
        # Calculate the number of ways by counting number of dividers possible between each pair of sections
        ways = 1
        for i in range(2, len(seat_indices), 2):
            # Calculate the plants between the end of the previous pair and the start of the next pair
            prev_seat_end = seat_indices[i - 1]
            next_seat_start = seat_indices[i]
            # Count available slots for placing new dividers
            ways *= (next_seat_start - prev_seat_end)
            ways %= MOD
        
        return ways