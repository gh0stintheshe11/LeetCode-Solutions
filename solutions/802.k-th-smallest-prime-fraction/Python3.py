class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        from heapq import heappush, heappop

        n = len(arr)
        heap = []

        for i in range(n):
            for j in range(i + 1, n):
                heappush(heap, (arr[i] / arr[j], arr[i], arr[j]))

        while k > 1:
            heappop(heap)
            k -= 1

        _, num, denom = heappop(heap)
        return [num, denom]