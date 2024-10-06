class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def cost_to_make_non_decreasing(nums):
            operations = 0
            max_heap = []
            for num in nums:
                if max_heap and -max_heap[0] > num:
                    operations += -heapq.heappop(max_heap) - num
                    heapq.heappush(max_heap, -num)
                heapq.heappush(max_heap, -num)
            return operations
        
        def cost_to_make_non_increasing(nums):
            return cost_to_make_non_decreasing([-num for num in nums])
        
        return min(cost_to_make_non_decreasing(nums), cost_to_make_non_increasing(nums))