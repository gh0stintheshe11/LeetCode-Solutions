class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)

        arr = [0]*(k+1) #min
        cts = defaultdict(int)
        for i in range(n//2):
            a,b = nums[i],nums[n-i-1]
            if a<b:
                a,b = b,a
            cts[a-b]+=1 # diff ct
            p = max(k-b,a) # max we can change
            arr[p]+=1
        
        mn = n//2-cts[0]
        for i in range(1,k+1):
            arr[i]+=arr[i-1]

        for i in range(1,k+1):
            mn = min(mn,2*arr[i-1]+arr[-1]-arr[i-1]-cts[i])
        return mn