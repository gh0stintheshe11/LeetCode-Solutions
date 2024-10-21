class Solution {
public:
    string shortestPalindrome(string s) {
        string rev_s = s;
        reverse(rev_s.begin(), rev_s.end());
        string l = s + "#" + rev_s;
        vector<int> p(l.size(), 0);
        
        for (int i = 1; i < l.size(); i++) {
            int j = p[i - 1];
            while (j > 0 && l[i] != l[j]) {
                j = p[j - 1];
            }
            if (l[i] == l[j]) {
                j++;
            }
            p[i] = j;
        }
        
        return rev_s.substr(0, s.size() - p.back()) + s;
    }
};