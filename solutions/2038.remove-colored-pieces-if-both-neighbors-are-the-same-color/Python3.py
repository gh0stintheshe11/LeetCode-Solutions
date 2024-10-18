class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = 0
        bob_moves = 0
        n = len(colors)
        
        i = 0
        while i < n:
            current_char = colors[i]
            length = 0
            while i < n and colors[i] == current_char:
                length += 1
                i += 1
            if length >= 3:
                if current_char == 'A':
                    alice_moves += length - 2
                else:
                    bob_moves += length - 2
        
        return alice_moves > bob_moves