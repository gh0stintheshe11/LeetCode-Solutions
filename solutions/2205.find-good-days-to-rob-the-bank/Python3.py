class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))
        
        non_increasing = [0] * n
        non_decreasing = [0] * n
        
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                non_decreasing[n - i - 1] = non_decreasing[n - i] + 1

        result = []
        for i in range(time, n - time):
            if non_increasing[i] >= time and non_decreasing[i] >= time:
                result.append(i)
        
        return result