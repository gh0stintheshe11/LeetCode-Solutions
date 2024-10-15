class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column, row = coordinates
        column_number = ord(column) - ord('a') + 1
        row_number = int(row)
        return (column_number + row_number) % 2 != 0