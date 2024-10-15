class Solution:
    def findScore(self, nums: List[int]) -> int:
        import heapq

        n = len(nums)
        min_heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(min_heap)

        marked = [False] * n
        score = 0

        while min_heap:
            value, index = heapq.heappop(min_heap)
            if marked[index]:
                continue
            score += value
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < n - 1:
                marked[index + 1] = True

        return score