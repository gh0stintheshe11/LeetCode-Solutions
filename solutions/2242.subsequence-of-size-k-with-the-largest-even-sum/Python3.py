
class Solution:
    def largestEvenSum(self, nums, k):
        odd, even = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort(reverse=True)
        odd.sort(reverse=True)

        if len(even) + len(odd) < k:
            return -1

        sum, ei, oi = 0, 0, 0

        if k % 2 != 0:
            if len(even):
                sum += even[ei]
                ei += 1
                k -= 1
            else:
                return -1

        while k > 0:
            odd_sum = -1
            even_sum = -1

            if oi + 1 < len(odd):
                odd_sum = odd[oi] + odd[oi+1]
            if ei + 1 < len(even):
                even_sum = even[ei] + even[ei+1]

            if odd_sum >= even_sum and odd_sum != -1:
                sum += odd_sum
                oi += 2
            elif even_sum >= odd_sum and even_sum != -1:
                sum += even_sum
                ei += 2
            else:
                return -1
            k -= 2

        return sum
        