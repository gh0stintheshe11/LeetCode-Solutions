class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.length() < p.length()) return result;
        
        vector<int> pCount(26, 0), sCount(26, 0);
        
        for (char c : p) 
            pCount[c - 'a']++;
        
        int pLength = p.length();
        
        for (int i = 0; i < s.length(); ++i) {
            sCount[s[i] - 'a']++;
            
            if (i >= pLength)
                sCount[s[i - pLength] - 'a']--;
            
            if (pCount == sCount)
                result.push_back(i - pLength + 1);
        }
        
        return result;
    }
};