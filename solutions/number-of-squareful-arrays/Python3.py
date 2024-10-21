class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:

        @lru_cache(10_000)
        def is_square(x: int) -> bool:
            if x & 2: return False
            return isqrt(x) ** 2 == x

        def dfs() -> None:
            if len(squares) == n: self.ans += 1

            for key in ctr:
                if not ctr[key]: continue
                if not squares or (squares[-1], key) in pairs:
                    squares.append(key)
                    ctr[key] -= 1
                    dfs()
                    ctr[key] += 1
                    squares.pop()
            return       

        n, self.ans = len(nums), 0
        ctr, squares = Counter(nums), []

        pairs = set((a, b) for a, b in 
                    product(ctr, ctr) if is_square(a + b))
        
        dfs()

        return self.ans