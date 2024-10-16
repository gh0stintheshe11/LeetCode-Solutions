class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int area1 = (ax2 - ax1) * (ay2 - ay1);
        int area2 = (bx2 - bx1) * (by2 - by1);
        
        int overlapWidth = std::max(0, std::min(ax2, bx2) - std::max(ax1, bx1));
        int overlapHeight = std::max(0, std::min(ay2, by2) - std::max(ay1, by1));
        int overlapArea = overlapWidth * overlapHeight;
        
        return area1 + area2 - overlapArea;
    }
};