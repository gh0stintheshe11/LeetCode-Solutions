class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        from collections import defaultdict
        
        def is_valid(count):
            min_count = min(filter(lambda x: x > 0, count))
            return all(x == 0 or x == min_count for x in count)

        unique_substrings = set()
        
        for start in range(len(s)):
            count = [0] * 10
            for end in range(start, len(s)):
                digit = int(s[end])
                count[digit] += 1
                if is_valid(count):
                    unique_substrings.add(s[start:end + 1])

        return len(unique_substrings)