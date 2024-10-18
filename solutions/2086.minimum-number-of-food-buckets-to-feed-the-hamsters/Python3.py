class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        buckets = 0
        i = 0

        while i < n:
            if hamsters[i] == 'H':
                if i + 1 < n and hamsters[i + 1] == '.':
                    # Place bucket at i + 1
                    buckets += 1
                    i += 2  # Skip this and the next index as it's covered
                elif i > 0 and hamsters[i - 1] == '.':
                    # Place bucket at i - 1
                    buckets += 1
                else:
                    # No place to put a bucket, impossible to feed this hamster
                    return -1
            i += 1

        return buckets