class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        mod = 10**9+7
        m = max(nums)
        n = len(nums)
        minHeap = []
        for i in range(len(nums)):
            heapq.heappush(minHeap,[nums[i],i])
        while k and minHeap[0][0]*multiplier <= m:
            value,index = heapq.heappop(minHeap)
            value = value*multiplier
            value = value%mod
            heapq.heappush(minHeap,[value,index])
            k -= 1

        vals = sorted(minHeap)
        j,k = k//n,k%n

        # Each element is multiplied by j times of multiplier
        for i in range(len(nums)):
            vals[i][0] = vals[i][0]*pow(multiplier,j,mod)%mod

        # for last cycle or remaining part
        for i in range(k):
            vals[i][0] = vals[i][0]*multiplier%mod

        ans = [0]*len(nums)

        for value,index in vals:
            ans[index] = value

        return ans