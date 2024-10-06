from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        combined = sorted(zip(aliceValues, bobValues), key=lambda x: -(x[0] + x[1]))
        alice_score = bob_score = 0
        
        for i in range(len(combined)):
            if i % 2 == 0:  # Alice's turn
                alice_score += combined[i][0]
            else:  # Bob's turn
                bob_score += combined[i][1]
        
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        else:
            return 0