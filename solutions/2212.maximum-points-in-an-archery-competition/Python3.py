from typing import List

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = len(aliceArrows)
        max_score = 0
        best_allocation = [0] * n
        
        # Iterate over all subsets of target sections
        for mask in range(1 << n):
            used_arrows = 0
            score = 0
            allocation = [0] * n
            
            # Check each section in the subset
            for i in range(n):
                if mask & (1 << i):  # If the i-th bit is set in mask
                    needed_arrows = aliceArrows[i] + 1
                    if used_arrows + needed_arrows <= numArrows:
                        used_arrows += needed_arrows
                        allocation[i] = needed_arrows
                        score += i
            
            # Check if this allocation gives a better score
            if score > max_score:
                max_score = score
                best_allocation = allocation.copy()
        
        # Distribute any remaining arrows to any section (say, section 0)
        remaining_arrows = numArrows - sum(best_allocation)
        for i in range(n):
            if remaining_arrows > 0:
                best_allocation[i] += remaining_arrows
                break
        
        return best_allocation