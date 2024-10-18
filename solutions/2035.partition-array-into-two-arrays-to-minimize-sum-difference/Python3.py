from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum // 2

        def generate_sums(nums: List[int]) -> List[List[int]]:
            # Generate all sums and store in separate lists based on the count of numbers included
            n = len(nums)
            sums = [[] for _ in range(n+1)]
            for i in range(1 << n):  # Loop from 0 to 2^n
                sum_val, count = 0, 0
                for j in range(n):
                    if i & (1 << j):
                        sum_val += nums[j]
                        count += 1
                sums[count].append(sum_val)
            return sums

        def combine_and_minimize_diff(sums1, sums2):
            # Combine the two sets of sums to find the minimal difference
            min_diff = float('inf')
            for k in range(n+1):
                sums2_k = sorted(sums2[n-k])

                for sum1 in sums1[k]:
                    current_target = total_sum // 2 - sum1
                    
                    # Binary search for the best sum in sums2_k that gets closest to current_target
                    lo, hi = 0, len(sums2_k) - 1
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        if sums2_k[mid] < current_target:
                            lo = mid + 1
                        else:
                            hi = mid - 1

                    # Calculate possibility in bounds: lo and lo-1 indices
                    for idx in [lo, lo - 1]:
                        if 0 <= idx < len(sums2_k):
                            cur_sum = sum1 + sums2_k[idx]
                            min_diff = min(min_diff, abs(total_sum - 2 * cur_sum))
                        
            return min_diff

        nums1 = nums[:n]
        nums2 = nums[n:]

        # Generate all possible sums for every combination count
        sums1 = generate_sums(nums1)
        sums2 = generate_sums(nums2)

        return combine_and_minimize_diff(sums1, sums2)