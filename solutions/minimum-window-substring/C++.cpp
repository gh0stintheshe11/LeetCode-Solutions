class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";
        
        unordered_map<char, int> t_freq;
        for (char c : t) t_freq[c]++;
        
        int required = t_freq.size();
        
        int l = 0, r = 0;
        int formed = 0;
        unordered_map<char, int> window_freq;
        
        int min_len = INT_MAX;
        int start = 0;
        
        while (r < s.size()) {
            char c = s[r];
            window_freq[c]++;
            
            if (t_freq.count(c) && window_freq[c] == t_freq[c]) {
                formed++;
            }
            
            while (l <= r && formed == required) {
                c = s[l];
                
                if (r - l + 1 < min_len) {
                    min_len = r - l + 1;
                    start = l;
                }
                
                window_freq[c]--;
                if (t_freq.count(c) && window_freq[c] < t_freq[c]) {
                    formed--;
                }
                
                l++;
            }
            
            r++;
        }
        
        return min_len == INT_MAX ? "" : s.substr(start, min_len);
    }
};