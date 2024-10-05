class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = [0] * 10
        guess_count = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1

        for i in range(10):
            cows += min(secret_count[i], guess_count[i])
        
        return f"{bulls}A{cows}B"