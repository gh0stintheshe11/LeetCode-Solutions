class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) return false;
        
        unordered_map<char, char> s_to_t, t_to_s;
        
        for (int i = 0; i < s.length(); ++i) {
            char sc = s[i];
            char tc = t[i];
            
            if ((s_to_t.count(sc) && s_to_t[sc] != tc) || 
                (t_to_s.count(tc) && t_to_s[tc] != sc)) {
                return false;
            }
            
            s_to_t[sc] = tc;
            t_to_s[tc] = sc;
        }
        
        return true;
    }
};