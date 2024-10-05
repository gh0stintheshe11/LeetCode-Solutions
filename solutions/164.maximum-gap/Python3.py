class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        a, b = min(nums), max(nums)
        if a == b:
            return 0

        size = max(1, (b - a) // (len(nums) - 1))
        bucket_count = (b - a) // size + 1
        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            bucket_idx = (num - a) // size
            bucket = buckets[bucket_idx]
            if bucket[0] is None:
                bucket[0] = bucket[1] = num
            else:
                bucket[0] = min(bucket[0], num)
                bucket[1] = max(bucket[1], num)

        max_gap = 0
        prev_max = a
        for bucket in buckets:
            if bucket[0] is not None:
                max_gap = max(max_gap, bucket[0] - prev_max)
                prev_max = bucket[1]

        return max_gap