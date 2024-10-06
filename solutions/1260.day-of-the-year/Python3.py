class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        
        # Check if it is a leap year
        def is_leap_year(y: int) -> bool:
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
        
        # Number of days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Adjust February for leap years
        if is_leap_year(year):
            days_in_month[1] = 29
        
        # Calculate day of the year
        return sum(days_in_month[:month - 1]) + day