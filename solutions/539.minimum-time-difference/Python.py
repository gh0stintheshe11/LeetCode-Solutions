class Solution(object):
    def findMinDifference(self, timePoints):
        def convert_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        times_in_minutes = [convert_to_minutes(time) for time in timePoints]
        times_in_minutes.sort()

        # Initialize the minimum difference as large value
        min_difference = float('inf')
        n = len(times_in_minutes)

        for i in range(1, n):
            min_difference = min(min_difference, times_in_minutes[i] - times_in_minutes[i - 1])

        # Check the circular case (last element and first element looping)
        circular_difference = (1440 + times_in_minutes[0] - times_in_minutes[-1]) % 1440
        min_difference = min(min_difference, circular_difference)

        return min_difference