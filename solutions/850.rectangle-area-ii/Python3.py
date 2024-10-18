[]
class Solution:
    def get_y_range(self, active_intervals):
        cur_area = 0
        y_last = -1
        active_intervals.sort()
        for y_start, y_end in active_intervals:
            area = max(0, y_end - max(y_start, y_last))
            cur_area += area
            y_last = max(y_end, y_last)
        return cur_area

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        START = 0
        END = 1
        for x1,y1,x2,y2 in rectangles:
            events.append((x1, y1, y2, START))
            events.append((x2, y1, y2, END))

        events.sort()
        cur_intervals = []
        total_area = 0
        x_last = events[0][0]
        for x, y_start, y_end, typ in events:
            y_area = self.get_y_range(cur_intervals)
            total_area +=  y_area * (x - x_last)
            if typ == START:
                cur_intervals.append((y_start, y_end))
            else:
                cur_intervals.remove((y_start, y_end))
            x_last = x
        return total_area % (10**9 + 7)
