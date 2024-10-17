class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        ans = 0
        low = 1
        high = 10**15
        while low <= high:
            mid = (low + high) // 2
            binary = bin(mid)[2:]
            count = 0
            for multiplier in range(x, len(binary) + 1, x):
                value = 2**(multiplier - 1)
                total_numbers = (mid - value) + 1
                quotient = total_numbers // value
                count += ((quotient + 1) // 2) * value
                
                if quotient % 2 == 0:
                    count += (total_numbers % value)       
            if count > k:
                high = mid - 1
            if count <= k:
                low = mid + 1
                ans = mid
        return ans