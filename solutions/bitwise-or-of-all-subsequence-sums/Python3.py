class Solution:
    def subsequenceSumOr(self, nums):
        ans, running_sum, res = set(), 0, []

        for i in nums:
            running_sum += i
            res.append(running_sum)
            res.append(i)

        val = 0

        for i in res:
            val = val | i

        return val