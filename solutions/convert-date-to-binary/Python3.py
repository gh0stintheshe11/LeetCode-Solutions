class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        year_binary = bin(int(year))[2:]
        month_binary = bin(int(month))[2:]
        day_binary = bin(int(day))[2:]
        return f"{year_binary}-{month_binary}-{day_binary}"