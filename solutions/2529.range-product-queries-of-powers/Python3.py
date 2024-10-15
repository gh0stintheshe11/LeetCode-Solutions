class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Create the powers array
        powers = []
        current = 1
        while n > 0:
            if n & 1:
                powers.append(current)
            current *= 2
            n >>= 1
        
        # Answer the queries
        answers = []
        for left, right in queries:
            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD
            answers.append(product)
        
        return answers