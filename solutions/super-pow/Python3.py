class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        def powMod(x: int, n: int, mod: int) -> int:
            res = 1
            x %= mod
            while n > 0:
                if n % 2 == 1:
                    res = (res * x) % mod
                x = (x * x) % mod
                n //= 2
            return res
        
        def superPowMod(a: int, b: List[int], mod: int) -> int:
            if not b:
                return 1
            last_digit = b.pop()
            part1 = powMod(a, last_digit, mod)
            part2 = powMod(superPowMod(a, b, mod), 10, mod)
            return (part1 * part2) % mod
        
        return superPowMod(a, b, MOD)