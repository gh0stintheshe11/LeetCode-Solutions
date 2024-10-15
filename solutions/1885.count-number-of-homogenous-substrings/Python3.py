class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                total_count += (count * (count + 1)) // 2
                total_count %= MOD
                count = 1

        # add the last counted homogenous substring block
        total_count += (count * (count + 1)) // 2
        total_count %= MOD

        return total_count