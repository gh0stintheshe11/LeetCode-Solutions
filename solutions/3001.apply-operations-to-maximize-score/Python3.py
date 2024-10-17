from typing import List
from math import sqrt
from functools import cache

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def sieve(n):
            limit = int(sqrt(n))
            isPrime = [True] * (limit+1)
            isPrime[0] = isPrime[1] = False
            for i in range(2, int(sqrt(limit+1))):
                if not isPrime[i]:
                    continue
                for j in range(i+i, limit+1, i):
                    isPrime[j] = False
            return [i for i, x in enumerate(isPrime) if x]

        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
            53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 
            109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 
            173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
            233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 
            293, 307, 311, 313
        ]

        @cache
        def primeScore(x):
            ret = 0
            if x == 1:
                return 0
            for p in primes:
                if x % p == 0:
                    ret += 1
                    while x % p == 0:
                        x //= p
                if x == 1:
                    break
            return ret if x == 1 else ret + 1

        scores = tuple(map(primeScore, nums))

        left = [0] * len(nums)
        st = [(99999, -1)]
        for i, score in enumerate(scores):
            while st[-1][0] < score:
                st.pop()
            left[i] = st[-1][1]
            if st[-1][0] == score:
                st.pop()
            st.append((score, i))

        right = [0] * len(nums)
        st = [(99999, len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            score = scores[i]
            while st[-1][0] <= score:
                st.pop()
            right[i] = st[-1][1]
            st.append((score, i))

        mod = int(1e9 + 7)

        @cache
        def powMod(a, b):
            if b == 0:
                return 1
            if b == 1:
                return a
            pm = powMod(a, b // 2)
            return (pm * pm * (a if b & 1 else 1)) % mod

        val_ind = sorted(([x, i] for i, x in enumerate(nums)), key=lambda x: -x[0])
        ret = 1
        for val, ind in val_ind:
            if val == 1:
                break
            thisScore = scores[ind]
            i = left[ind]
            j = right[ind]
            b = (ind - i) * (j - ind)
            c = min(k, b)
            e = pow(val, c, mod)
            ret *= e
            ret %= mod
            k -= c
            if k == 0:
                return ret
        return ret