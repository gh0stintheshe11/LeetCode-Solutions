class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calculate_score(player):
            n = len(player)
            score = 0
            for i in range(n):
                if (i > 0 and player[i-1] == 10) or (i > 1 and player[i-2] == 10):
                    score += 2 * player[i]
                else:
                    score += player[i]
            return score
        
        score1 = calculate_score(player1)
        score2 = calculate_score(player2)
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0