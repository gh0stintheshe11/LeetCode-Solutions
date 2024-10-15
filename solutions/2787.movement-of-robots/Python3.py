class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Calculate final positions after d seconds
        final_positions = []
        for i in range(n):
            if s[i] == 'L':
                final_positions.append(nums[i] - d)
            else:
                final_positions.append(nums[i] + d)
        
        # Sort final_positions to easily compute pairwise distances as they would be ordered
        final_positions.sort()

        # Compute sum of distances between all pairs
        total_distance = 0
        sum_left = 0
        
        for i in range(n):
            # For each position, calculate its contribution to the total sum of distances
            # Contribution of final_positions[i] = i * final_positions[i] - sum_left
            total_distance = (total_distance + i * final_positions[i] - sum_left) % MOD
            sum_left = (sum_left + final_positions[i]) % MOD
        
        return total_distance