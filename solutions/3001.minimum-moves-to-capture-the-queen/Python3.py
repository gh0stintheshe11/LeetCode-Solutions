class Solution:
    def minMovesToCaptureTheQueen(self, rx, ry, bx, by, qx, qy):
        def inside(a, b, c):
            return min(b, c) <= a <= max(b, c)

        if rx == qx:
            if bx != rx or not inside(by, ry, qy):
                return 1
        if ry == qy:
            if by != ry or not inside(bx, rx, qx):
                return 1
        if bx-by == qx-qy:
            if rx-ry != qx-qy or not inside(rx, bx, qx):
                return 1
        if bx+by == qx+qy:
            if rx+ry != qx+qy or not inside(rx, bx, qx):
                return 1

        return 2