class Solution:
    def minAnagramLength(self, s: str) -> int:
        from collections import Counter

        def is_valid(length):
            if len(s) % length != 0:
                return False
            part_count = len(s) // length
            part_counter = Counter(s[:length])
            for i in range(1, part_count):
                if Counter(s[i*length:(i+1)*length]) != part_counter:
                    return False
            return True

        n = len(s)
        for length in range(1, n + 1):
            if is_valid(length):
                return length

        return n