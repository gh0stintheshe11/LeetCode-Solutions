class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        from itertools import accumulate

        # Pair nums and cost, then sort by nums to calculate the target median
        nums_cost = sorted(zip(nums, cost))
        
        # Calculate the prefix sums of the costs
        prefix_cost = list(accumulate(c for _, c in nums_cost))
        total_cost = prefix_cost[-1]

        # Find weighted median
        half_cost = total_cost // 2
        median_index = 0
        while prefix_cost[median_index] <= half_cost:
            median_index += 1

        # Determine the median value for nums
        target = nums_cost[median_index][0]

        # Calculate the minimum cost to make all elements equal to the target value
        return sum(abs(num - target) * c for num, c in nums_cost)