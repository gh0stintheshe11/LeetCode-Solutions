class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import defaultdict
        
        # Step 1: Collect all segments of the same character
        segments = []
        i = 0
        n = len(text)
        
        while i < n:
            start = i
            while i < n and text[i] == text[start]:
                i += 1
            segments.append((text[start], i - start))
        
        # Step 2: Collect counts of each character
        count = defaultdict(int)
        for c in text:
            count[c] += 1
        
        max_len = 1
        
        # Step 3: Calculate the maximum length we can achieve
        for idx, (char, length) in enumerate(segments):
            # Consider the length of a block of repeating characters
            max_len = max(max_len, length)
            
            # Check if we can extend this block by connecting two blocks
            if idx < len(segments) - 2:
                next_char, next_length = segments[idx + 2]
                if next_char == char and segments[idx + 1][1] == 1:  # only if there's one char blocking
                    # Combine current and next similar segments
                    if count[char] > length + next_length:
                        max_len = max(max_len, length + next_length + 1)
                    else:
                        max_len = max(max_len, length + next_length)
            
            # Check if we can extend this block by taking one more character of the same type
            if count[char] > length:
                max_len = max(max_len, length + 1)

        return max_len