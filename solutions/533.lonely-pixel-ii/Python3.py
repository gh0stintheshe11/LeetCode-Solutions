class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        from collections import defaultdict
        
        row_count = [0] * len(picture)
        col_count = [0] * len(picture[0])
        row_patterns = defaultdict(int)

        # Count the number of 'B' in each row and column
        for i in range(len(picture)):
            row_str = ''.join(picture[i])
            row_patterns[row_str] += 1
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1

        result = 0
        
        # Check each row and column
        for i in range(len(picture)):
            if row_count[i] == target:
                row_str = ''.join(picture[i])
                if row_patterns[row_str] == target:
                    for j in range(len(picture[0])):
                        if picture[i][j] == 'B' and col_count[j] == target:
                            result += 1
        
        return result