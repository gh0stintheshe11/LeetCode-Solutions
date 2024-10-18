class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Sort the cuts
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Calculate the maximum difference between consecutive horizontal cuts
        max_h_cut = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h_cut = max(max_h_cut, horizontalCuts[i] - horizontalCuts[i - 1])
        
        # Calculate the maximum difference between consecutive vertical cuts
        max_v_cut = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_v_cut = max(max_v_cut, verticalCuts[i] - verticalCuts[i - 1])
        
        # Return the max area modulo 10^9 + 7
        return (max_h_cut * max_v_cut) % MOD