class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        N = len(s)
        s = [int(c) for c in s]

        # Initialize prefix and suffix pair counts
        prefix_pair_counts = [[[0]*10 for _ in range(10)] for _ in range(N)]
        suffix_pair_counts = [[[0]*10 for _ in range(10)] for _ in range(N)]

        # Count of digits up to current position
        count_prefix = [0]*10

        # Compute prefix pair counts
        for i in range(N):
            if i > 0:
                # Copy previous counts
                for a in range(10):
                    for b in range(10):
                        prefix_pair_counts[i][a][b] = prefix_pair_counts[i-1][a][b]
            d = s[i]
            # Update counts for pairs ending at current digit
            for a in range(10):
                prefix_pair_counts[i][a][d] += count_prefix[a]
            # Update count of current digit
            count_prefix[d] +=1

        # Count of digits from current position to end
        count_suffix = [0]*10

        # Compute suffix pair counts
        for i in range(N-1, -1, -1):
            if i < N-1:
                # Copy next counts
                for a in range(10):
                    for b in range(10):
                        suffix_pair_counts[i][a][b] = suffix_pair_counts[i+1][a][b]
            d = s[i]
            # Update counts for pairs starting at current digit
            for b in range(10):
                suffix_pair_counts[i][d][b] += count_suffix[b]
            # Update count of current digit
            count_suffix[d] +=1

        # Compute total number of palindromic subsequences
        total = 0
        for i in range(2, N-2):
            for a in range(10):
                for b in range(10):
                    total += (prefix_pair_counts[i-1][a][b] * suffix_pair_counts[i+1][b][a]) % MOD
                    total %= MOD

        return total