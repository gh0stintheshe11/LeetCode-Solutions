class Solution {
public:
    int countSegments(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); ++i) {
            if ((i == 0 || s[i - 1] == ' ') && s[i] != ' ') {
                count++;
            }
        }
        return count;
    }
};