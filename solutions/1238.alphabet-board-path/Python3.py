class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = {
            'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (0, 3), 'e': (0, 4),
            'f': (1, 0), 'g': (1, 1), 'h': (1, 2), 'i': (1, 3), 'j': (1, 4),
            'k': (2, 0), 'l': (2, 1), 'm': (2, 2), 'n': (2, 3), 'o': (2, 4),
            'p': (3, 0), 'q': (3, 1), 'r': (3, 2), 's': (3, 3), 't': (3, 4),
            'u': (4, 0), 'v': (4, 1), 'w': (4, 2), 'x': (4, 3), 'y': (4, 4),
            'z': (5, 0)
        }
        
        x, y = 0, 0
        result = []
        
        for char in target:
            nx, ny = board[char]
            
            if y > ny:
                result.append('L' * (y - ny))
            if x > nx:
                result.append('U' * (x - nx))
            if y < ny:
                result.append('R' * (ny - y))
            if x < nx:
                result.append('D' * (nx - x))
                
            result.append('!')
            
            x, y = nx, ny
            
        return ''.join(result)