class Solution {
public:
    int strStr(string haystack, string needle) {
        int hlen = haystack.length();
        int nlen = needle.length();
        
        if (nlen == 0) return 0;
        if (hlen < nlen) return -1;
        
        for (int i = 0; i <= hlen - nlen; ++i) {
            if (haystack.substr(i, nlen) == needle) {
                return i;
            }
        }
        
        return -1;
    }
};