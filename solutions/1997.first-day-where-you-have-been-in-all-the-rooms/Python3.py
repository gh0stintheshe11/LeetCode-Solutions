class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nextVisit)
        days = [0] * n
        for i in range(1, n):
            days[i] = (2 * days[i - 1] + 2 - days[nextVisit[i - 1]] + MOD) % MOD
        return days[n - 1]