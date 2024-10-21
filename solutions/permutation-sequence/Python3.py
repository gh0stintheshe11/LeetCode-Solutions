class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        factorial = [1]*(n+1)
        for i in range(1,n+1):
            factorial[i]*=i*factorial[i-1]
        k -= 1
        ans = []
        for i in range(n,0,-1):
            id = k // factorial[i-1]
            k %= factorial[i-1]
            ans.append(nums[id])
            nums.pop(id)
        return ''.join(ans)