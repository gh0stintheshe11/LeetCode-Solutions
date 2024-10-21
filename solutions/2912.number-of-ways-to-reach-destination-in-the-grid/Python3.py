class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        MOD = (10 ** 9) + 7
        M, N = n, m

        @cache
        def calc(sameI, sameJ, k):
            if k == 1:
                if sameI and sameJ:
                    return -float("inf")

                if sameI:
                    return 1

                if sameJ:
                    return 1 
                    
                return -float("inf")

            total = 0

            if sameI:
                total += max(0, (calc(1 ^ sameI, sameJ, k - 1) * (M - 1)) % MOD)
            if not sameI:
                total += max(0, (calc(1 ^ sameI, sameJ, k - 1)) % MOD)
                total += max(0, (calc(sameI, sameJ, k - 1) * (M - 2)) % MOD)

            if sameJ:
                total += max(0, (calc(sameI, 1 ^ sameJ, k - 1) * (N - 1)) % MOD)

            if not sameJ:
                total += max(0, (calc(sameI, 1 ^ sameJ, k - 1)) % MOD)

                total += max(0, (calc(sameI, sameJ, k - 1) * (N - 2)) % MOD)

            return total % MOD
        
        return max(calc(int(source[0] == dest[0]), int(source[1] == dest[1]), k), 0)