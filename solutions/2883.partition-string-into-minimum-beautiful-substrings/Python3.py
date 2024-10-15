class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # Pre-compute the binary representations of powers of 5 up to 5^6 (since 5^7 is 128, but max binary "111111111111111" is 32767)
        powers_of_5 = {bin(5**i)[2:] for i in range(7)}

        # Memoize results for each starting index
        memo = {}

        # Define a recursive function to find minimum beautiful substrings from given start index
        def solve(start):
            if start == len(s):
                return 0
            
            if start in memo:
                return memo[start]

            min_parts = float('inf')
            for end in range(start + 1, len(s) + 1):
                # Get the current substring
                substring = s[start:end]
                # Check if a beautiful substring (must not start with '0' unless it's "0" itself)
                if substring in powers_of_5:
                    result = solve(end)
                    if result != -1:  # valid following partition
                        min_parts = min(min_parts, 1 + result)
            
            memo[start] = -1 if min_parts == float('inf') else min_parts
            return memo[start]

        # Start from beginning of the string
        result = solve(0)
        return result if result != float('inf') else -1