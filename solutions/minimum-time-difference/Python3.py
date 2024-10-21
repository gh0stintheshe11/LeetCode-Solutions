class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time into minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)

        # Sort the time in minutes
        minutes.sort()

        # Initialize minimum difference to a large number
        min_diff = float('inf')

        # Compare each consecutive time difference
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        # Consider the circular difference between the last and first
        circular_diff = (1440 + minutes[0] - minutes[-1])
        min_diff = min(min_diff, circular_diff)

        return min_diff