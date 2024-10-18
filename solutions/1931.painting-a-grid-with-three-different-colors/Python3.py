class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def generate_patterns(row, last_color, pattern, patterns):
            if row == m:
                patterns.append(pattern)
                return
            for color in range(3):
                if color != last_color:
                    generate_patterns(row + 1, color, pattern * 3 + color, patterns)
        
        possible_patterns = []
        generate_patterns(0, -1, 0, possible_patterns)

        def are_compatible(p1, p2):
            for i in range(m):
                if (p1 % 3) == (p2 % 3):
                    return False
                p1 //= 3
                p2 //= 3
            return True

        pattern_index = {pattern: idx for idx, pattern in enumerate(possible_patterns)}
        num_patterns = len(possible_patterns)
        
        adj = [[] for _ in range(num_patterns)]
        for idx1, p1 in enumerate(possible_patterns):
            for idx2, p2 in enumerate(possible_patterns):
                if are_compatible(p1, p2):
                    adj[idx1].append(idx2)

        dp = [1] * num_patterns
        for _ in range(n - 1):
            new_dp = [0] * num_patterns
            for i in range(num_patterns):
                for j in adj[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD