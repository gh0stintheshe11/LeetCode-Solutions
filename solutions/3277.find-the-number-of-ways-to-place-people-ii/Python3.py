from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = [y for _,y in sorted((x, -y) for x, y in points)]

        def solve(i, j):
            if j < i + 2: return 0
            if j == i + 2: return int(points[i] <= points[i+1])
            k = (i+j) // 2
            ans = solve(i, k) + solve(k, j)
            
            intervals = []
            # Left intervals
            seen = SortedList([inf])
            for q in range(k-1, i-1, -1):
                y = points[q]
                prev = seen.bisect_left(y)
                if seen[prev] == y: continue
                intervals.append((y, 0, seen[prev]))
                seen.add(y)
            
            # Right intervals
            seen = SortedList([-inf])
            for y in points[k:j]:
                prev = seen.bisect_right(y) - 1
                if seen[prev] == y: continue
                intervals.append((seen[prev], 1, y))
                seen.add(y)

            intervals.sort()

            right_ends = SortedList()
            for start, is_right, end in intervals:
                if is_right:
                    right_ends.add(end)
                else:
                    ans += right_ends.bisect_left(end) - right_ends.bisect_left(start)
            return ans
        
        return solve(0, len(points))