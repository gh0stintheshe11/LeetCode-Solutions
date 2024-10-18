class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def find_first_positive(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        def find_last_negative(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        first_positive_index = find_first_positive(nums)
        last_negative_index = find_last_negative(nums)

        num_positives = len(nums) - first_positive_index
        num_negatives = last_negative_index + 1

        return max(num_positives, num_negatives)