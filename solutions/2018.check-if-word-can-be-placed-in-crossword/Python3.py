class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)

        def fits(sequence, word):
            if len(sequence) != word_len:
                return False
            for x, y in zip(sequence, word):
                if x != ' ' and x != y:
                    return False
            return True

        def get_sequence_from_board(x, y, dx, dy):
            sequence = []
            while 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                sequence.append(board[x][y])
                x += dx
                y += dy
            return sequence

        for i in range(m):
            for j in range(n):
                if board[i][j] != '#':
                    # Check horizontally to the right
                    if j == 0 or board[i][j - 1] == '#':
                        sequence = get_sequence_from_board(i, j, 0, 1)
                        if fits(sequence, word) or fits(sequence, word[::-1]):
                            return True

                    # Check vertically downwards
                    if i == 0 or board[i - 1][j] == '#':
                        sequence = get_sequence_from_board(i, j, 1, 0)
                        if fits(sequence, word) or fits(sequence, word[::-1]):
                            return True
                        
        return False