class Solution {
public:
    int longestSubstring(string s, int k) {
        return longestSubstringHelper(s, 0, s.length(), k);
    }
    
    int longestSubstringHelper(const string& s, int start, int end, int k) {
        if (end - start < k) return 0; // Not enough length for a valid substring
        
        vector<int> count(26, 0);
        for (int i = start; i < end; ++i) {
            count[s[i] - 'a']++;
        }
        
        for (int mid = start; mid < end; ++mid) {
            if (count[s[mid] - 'a'] >= k) continue;
            
            int midNext = mid + 1;
            while (midNext < end && count[s[midNext] - 'a'] < k) midNext++;
            
            return max(longestSubstringHelper(s, start, mid, k),
                       longestSubstringHelper(s, midNext, end, k));
        }
        
        return end - start;
    }
};