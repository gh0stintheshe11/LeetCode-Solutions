class Solution {
public:
    bool detectCapitalUse(string word) {
        int n = word.length();
        if (n == 0) return true;
        
        bool allUpperCase = true, allLowerCase = true, firstUpperRestLower = true;
        
        if (!isupper(word[0])) {
            firstUpperRestLower = false;
        }
        
        for (int i = 0; i < n; ++i) {
            if (!isupper(word[i])) {
                allUpperCase = false;
            } else {
                allLowerCase = false;
            }
            if (i > 0 && isupper(word[i])) {
                firstUpperRestLower = false;
            }
        }
        
        return allUpperCase || allLowerCase || firstUpperRestLower;
    }
};