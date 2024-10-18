class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        from collections import Counter
        from math import comb

        MOD = 10**9 + 7

        # Count frequencies of each character
        frequency = Counter(s)
        freq_values = list(frequency.values())

        # Impossible to select k unique letters
        if k > len(freq_values):
            return 0

        # Sort frequencies descending
        freq_values.sort(reverse=True)

        # Calculate the maximum beauty and determine boundaries
        max_beauty = sum(freq_values[:k])
        min_freq_needed = freq_values[k - 1]
        
        # Count how many times the min_freq_needed appears in the top k
        needed_count = sum(1 for f in freq_values[:k] if f == min_freq_needed)

        # Count total appearance of min_freq_needed
        total_min_freq_count = sum(1 for f in freq_values if f == min_freq_needed)

        # Calculate the number of k-subsequences with max beauty
        answer = pow(min_freq_needed, needed_count, MOD)

        # Factor in combination
        answer = (answer * comb(total_min_freq_count, needed_count)) % MOD

        for freq in freq_values[:k]:
            if freq != min_freq_needed:
                answer = (answer * freq) % MOD
        
        return answer