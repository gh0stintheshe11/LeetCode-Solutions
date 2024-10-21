class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        distinct_subarrays = set()

        for i in range(n):
            divisible_count = 0
            current_subarray = []
            for j in range(i, n):
                current_subarray.append(nums[j])
                if nums[j] % p == 0:
                    divisible_count += 1
                if divisible_count > k:
                    break
                distinct_subarrays.add(tuple(current_subarray))
        
        return len(distinct_subarrays)