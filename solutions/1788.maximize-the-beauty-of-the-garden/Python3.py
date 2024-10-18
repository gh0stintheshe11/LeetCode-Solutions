class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        first = {}
        last = {}
        for i in range(len(flowers)):
            if flowers[i] not in first:
                first[flowers[i]] = i
            else:
                last[flowers[i]] = i
        intervals = []
        for key in first:
            if key in last:
                intervals.append([key, first[key], last[key]])
        flowers[0] = max(flowers[0], 0)
        pref = [flowers[0]] 
        for i in range(1, len(flowers)):
            flowers[i] = max(flowers[i], 0)
            pref.append(pref[-1] + flowers[i])
        res = float('-inf')
        for interval in intervals:
            value, left, right = interval
            area = 0
            if left == 0:
                area = pref[right]
            else:
                area = pref[right] - pref[left - 1]
            if area == 0:
                res = max(res, 2 * value)
            elif value < 0:
                res = max(res, 2 * value + area)
            else:
                res = max(res, area)
        return res