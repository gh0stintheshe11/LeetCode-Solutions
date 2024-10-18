class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        freq = [0] * 32

        def add(n):
            for i in range(32):
                mask = 1 << i
                if (mask & n) != 0:
                    freq[i] += 1

        def remove(n):
            for i in range(32):
                mask = 1 << i
                if (mask & n) != 0:
                    freq[i] -= 1

        def check():
            r = 0
            for i, e in enumerate(freq):
                if e > 0:
                    r |= 1 << i
            return r >= k

        ans = float("inf")
        j = 0
        for i in range(len(nums)):
            add(nums[i])

            while check() and j <= i:
                ans = min(ans, i - j + 1)
                remove(nums[j])
                j += 1

        return ans if ans != float("inf") else -1