class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        using Point = pair<int, int>;
        map<Point, int> cornerFrequency;
        int min_x = INT_MAX, min_y = INT_MAX, max_x = INT_MIN, max_y = INT_MIN;
        long total_area = 0;

        for (const auto& rect : rectangles) {
            int x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3];
            min_x = min(min_x, x1);
            min_y = min(min_y, y1);
            max_x = max(max_x, x2);
            max_y = max(max_y, y2);
            total_area += (long)(x2 - x1) * (y2 - y1);

            cornerFrequency[{x1, y1}]++;
            cornerFrequency[{x1, y2}]++;
            cornerFrequency[{x2, y1}]++;
            cornerFrequency[{x2, y2}]++;
        }

        long expected_area = (long)(max_x - min_x) * (max_y - min_y);
        if (total_area != expected_area) return false;

        map<Point, int> expectedCorners = {
            {{min_x, min_y}, 1}, {{min_x, max_y}, 1},
            {{max_x, min_y}, 1}, {{max_x, max_y}, 1}
        };

        for (const auto& [corner, count] : cornerFrequency) {
            if (expectedCorners.count(corner)) {
                if (count != expectedCorners[corner]) return false;
            } else {
                if (count % 2 != 0) return false;
            }
        }

        return true;
    }
};