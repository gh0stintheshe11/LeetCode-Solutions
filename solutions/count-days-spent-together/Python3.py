class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Helper function to convert a date in "MM-DD" format to a day of the year
        def dateToDayOfYear(date: str) -> int:
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month, day = map(int, date.split('-'))
            return sum(month_days[:month-1]) + day

        # Convert all dates to days of the year
        startAlice = dateToDayOfYear(arriveAlice)
        endAlice = dateToDayOfYear(leaveAlice)
        startBob = dateToDayOfYear(arriveBob)
        endBob = dateToDayOfYear(leaveBob)

        # Calculate the overlap period
        startOverlap = max(startAlice, startBob)
        endOverlap = min(endAlice, endBob)

        # Return the number of overlapping days
        return max(0, endOverlap - startOverlap + 1)