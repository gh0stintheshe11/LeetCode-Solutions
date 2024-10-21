MOD = 10**9 + 7

def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

class Solution:
    def waysToFillArray(self, queries):
        max_n = max(n for n, k in queries)
        
        # Precompute factorials and inverses
        fact = [1] * (max_n + 100)  # Increase size to handle larger values
        for i in range(2, len(fact)):
            fact[i] = fact[i - 1] * i % MOD
        
        inv_fact = [1] * (max_n + 100)
        inv_fact[len(fact) - 1] = mod_inverse(fact[len(fact) - 1], MOD)
        for i in range(len(fact) - 2, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def count_factors(k):
            if k == 1:
                return {}
            factors = {}
            for i in range(2, int(k**0.5) + 1):
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors

        results = []
        for n, k in queries:
            if k == 1:
                results.append(1)
                continue
            
            factors = count_factors(k)
            total_ways = 1
            
            for prime, exponent in factors.items():
                total_ways *= (fact[n + exponent - 1] * inv_fact[exponent] % MOD) * inv_fact[n - 1] % MOD
                total_ways %= MOD
            
            results.append(total_ways)
        
        return results

