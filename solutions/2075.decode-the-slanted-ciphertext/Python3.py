class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText or rows == 0:
            return ""
        
        n = len(encodedText)
        cols = n // rows
        
        matrix = []
        index = 0
        for r in range(rows):
            row = encodedText[index:index+cols]
            matrix.append(row)
            index += cols
        
        decoded_chars = []
        for c in range(cols):
            for r in range(rows):
                if c + r < cols:
                    decoded_chars.append(matrix[r][c + r])
        
        return ''.join(decoded_chars).rstrip()