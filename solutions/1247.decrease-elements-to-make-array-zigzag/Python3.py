class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def moves_needed(start_idx: int) -> int:
            moves = 0
            for i in range(start_idx, len(nums), 2):
                left = nums[i - 1] if i - 1 >= 0 else float('inf')
                right = nums[i + 1] if i + 1 < len(nums) else float('inf')
                decrease_to = min(left, right) - 1
                if nums[i] >= decrease_to:
                    moves += nums[i] - decrease_to
            return moves

        return min(moves_needed(0), moves_needed(1))