class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int bytesToProcess = 0;

        for (int num : data) {
            if (bytesToProcess == 0) {
                if ((num >> 5) == 0b110) bytesToProcess = 1;
                else if ((num >> 4) == 0b1110) bytesToProcess = 2;
                else if ((num >> 3) == 0b11110) bytesToProcess = 3;
                else if ((num >> 7) != 0) return false;
            } else {
                if ((num >> 6) != 0b10) return false;
                bytesToProcess--;
            }
        }
        return bytesToProcess == 0;
    }
};