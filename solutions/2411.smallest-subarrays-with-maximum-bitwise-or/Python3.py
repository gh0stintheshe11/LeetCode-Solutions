class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last_position = [-1] * 32  # We only need 32 bits for each integer
        
        # Iterate from back to front
        for i in range(n - 1, -1, -1):
            # Update last positions for each bit
            for bit in range(32):
                if (nums[i] & (1 << bit)) != 0:
                    last_position[bit] = i

            # Calculate the maximum distance to achieve the max bitwise OR for the current position
            max_distance = 1
            for bit in range(32):
                if last_position[bit] != -1:
                    max_distance = max(max_distance, last_position[bit] - i + 1)

            answer[i] = max_distance
        
        return answer