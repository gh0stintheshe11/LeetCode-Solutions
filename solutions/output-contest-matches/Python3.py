class Solution:
    def findContestMatch(self, n: int) -> str:
        matches = [str(i) for i in range(1, n+1)]
        while n > 1:
            new_matches = []
            for i in range(n//2):
                new_matches.append(f"({matches[i]},{matches[n-1-i]})")
            matches = new_matches
            n //= 2
        return matches[0]