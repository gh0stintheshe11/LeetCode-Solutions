class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        arr = [[points[i][0], points[i][1], s[i]] for i in range(len(points))]
        ans = 0
        arr.sort(key=lambda x: max(abs(x[0]), abs(x[1])))
        length = -1
        chars = set()
        bad_end = False
        for i in range(len(arr)):
            if length < max(abs(arr[i][0]), abs(arr[i][1])):
                ans = i
                length = max(abs(arr[i][0]), abs(arr[i][1]))
            if arr[i][2] in chars:
                bad_end = True
                break
            else:
                chars.add(arr[i][2])
        if not bad_end:
            ans = len(arr)
        return ans