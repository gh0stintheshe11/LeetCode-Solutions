class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count1 = count2 = 0

        for i in range(n):
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'
            if s[i] != expected1:
                count1 += 1
            if s[i] != expected2:
                count2 += 1

        return min(count1, count2)