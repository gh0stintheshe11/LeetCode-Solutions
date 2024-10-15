class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def is_black(coordinate: str) -> bool:
            col, row = coordinate
            return (ord(col) - ord('a') + int(row)) % 2 == 0

        return is_black(coordinate1) == is_black(coordinate2)