class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        ones_count = s.count('1')
        
        if ones_count % 3 != 0:
            return 0

        if ones_count == 0:
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % MOD
        
        ones_per_partition = ones_count // 3
        first_cut_ways = second_cut_ways = 0
        ones_count = 0

        for char in s:
            if char == '1':
                ones_count += 1
                
            if ones_count == ones_per_partition:
                first_cut_ways += 1
            elif ones_count == 2 * ones_per_partition:
                second_cut_ways += 1
        
        return (first_cut_ways * second_cut_ways) % MOD