class Solution:
    def closest(self, points):
        n = len(points)
        mid = n // 2
        if n < 2:
            return float('inf'), float('inf'), float('inf')
        midP = points[n // 2]
        dl, pi, pj = self.closest(points[:mid])
        dr, qi, qj = self.closest(points[mid:])
        d, ri, rj = min((dl, pi, pj), (dr, qi, qj))
        strip = []
        for i in range(n):
            if abs(points[i][0] - midP[0]) <= d:
                strip.append(points[i])
        ds, si, sj = self.stripclosest(strip, d)
        si, sj = sorted([si, sj])
        if (ds, si, sj) <= (d, ri, rj):
            ri, rj = sorted([si, sj])
            d = ds
        ri, rj = sorted([ri, rj])
        return d, ri, rj

    def stripclosest(self, strip, d):
        min_d = d
        strip = sorted(strip, key=lambda x: (x[1], x[2]))
        m = len(strip)
        si, sj = float('inf'), float('inf')
        for i in range(m):
            for j in range(i + 1, m):
                if (strip[j][1] - strip[i][1]) > min_d:
                    break
                currd = abs(strip[j][1] - strip[i][1]) + abs(strip[j][0] - strip[i][0])
                curri, currj = sorted([strip[i][2], strip[j][2]])
                min_d, si, sj = min((min_d, si, sj), (currd, curri, currj))
        si, sj = sorted([si, sj])
        return min_d, si, sj

    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = float('inf'), float('inf')
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if (x, y) in seen:
                res = min(res, (seen[(x, y)], i))
            else:
                seen[(x, y)] = i
        if res[0] < float('inf'):
            return res
        points = [(x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2))]
        points.sort()
        mind, resi, resj = self.closest(points)

        return sorted([resi, resj])