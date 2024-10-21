class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        low = 1
        high = 10**9+1
        
        diff_val = x-y
        last_res = -1
        while low < high:
            mid = int((low+high)/2)
            rem_sum = 0
            for val in nums:
                if val>(mid*y):
                    rem_sum += math.ceil((val-mid*y)/diff_val)
            if rem_sum <= mid:
                last_res = mid
                high = mid
            else:
                low = mid + 1
        return last_res