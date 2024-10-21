class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        sort(strs.begin(), strs.end(), [](const string &a, const string &b) {
            return a.size() > b.size() || (a.size() == b.size() && a < b);
        });

        auto isSubsequence = [](const string &a, const string &b) {
            int i = 0;
            for (char c : b) {
                if (i < a.size() && a[i] == c) {
                    i++;
                }
            }
            return i == a.size();
        };

        for (int i = 0; i < strs.size(); ++i) {
            bool unique = true;
            for (int j = 0; j < strs.size(); ++j) {
                if (i != j && isSubsequence(strs[i], strs[j])) {
                    unique = false;
                    break;
                }
            }
            if (unique) {
                return strs[i].size();
            }
        }
        return -1;
    }
};