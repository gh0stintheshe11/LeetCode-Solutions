from typing import List

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        res = []
        for i in range(n - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                res.append(currentState[:i] + '--' + currentState[i + 2:])
        return res