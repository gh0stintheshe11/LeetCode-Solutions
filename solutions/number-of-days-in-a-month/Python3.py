class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month == 2:
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                return 29
            else:
                return 28
        elif month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        else:
            return 30