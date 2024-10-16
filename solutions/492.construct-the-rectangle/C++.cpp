class Solution {
public:
    vector<int> constructRectangle(int area) {
        int w = sqrt(area);
        while (area % w != 0) {
            w--;
        }
        int l = area / w;
        return {l, w};
    }
};