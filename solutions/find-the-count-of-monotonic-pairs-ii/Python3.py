class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        def findSmallest(num1, num2, n):
            low, high = num1, n

            while low <= high:
                mid = (low + high) // 2
                tmp2 = n - mid

                if tmp2 <= num2:
                    high = mid - 1
                else:
                    low = mid + 1

            return low
                
        MOD = 10 ** 9 + 7
        n = len(nums)
        last = nums[-1]
        dp = [1] * (last + 1)

        for i in range(n - 2, -1, -1):
            preSum = list(accumulate(dp, initial=0))
            num, prev = nums[i], nums[i + 1]
            tmp_dp = []
            toLook = -1
            for a1 in range(num + 1):
                if a1 > prev:
                    tmp_dp.extend([0] * (num - a1 + 1))
                    continue

                a2 = num - a1
                if toLook >= 0:
                    toLook += 1
                else:
                    toLook = findSmallest(a1, a2, prev)

                toAdd = preSum[-1] - preSum[toLook]
                tmp_dp.append(toAdd)

            dp = tmp_dp

        return sum(dp) % MOD