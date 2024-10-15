class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def fast_power(base: int, power: int) -> int:
            result = 1
            while power > 0:
                if power % 2:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                power //= 2
            return result

        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        return (fast_power(5, even_positions) * fast_power(4, odd_positions)) % MOD