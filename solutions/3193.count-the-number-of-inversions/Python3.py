class Solution:
    def numberOfPermutations(self, N: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        lookup = {}
        for u, v in requirements:
            lookup[u] = v

        @cache
        def calc(index, cur) -> int:
            if index == 0:
                if index not in lookup:
                    return cur == 0
                
                if lookup[index] != 0:
                    return 0

                return cur == 0

            if index in lookup and lookup[index] != cur:
                return 0

            total = 0
            for j in range(index + 1):
                nxt = cur - j
                if nxt < 0:
                    break
                total += calc(index - 1, nxt)
            
            return total

        return calc(N - 1, lookup[N - 1]) % MOD