class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> lastIndex(26, -1);
        vector<bool> inStack(26, false);
        
        for (int i = 0; i < s.size(); ++i) {
            lastIndex[s[i] - 'a'] = i;
        }
        
        string result;
        
        for (int i = 0; i < s.size(); ++i) {
            if (inStack[s[i] - 'a']) continue;
            
            while (!result.empty() && result.back() > s[i] && lastIndex[result.back() - 'a'] > i) {
                inStack[result.back() - 'a'] = false;
                result.pop_back();
            }
            
            result += s[i];
            inStack[s[i] - 'a'] = true;
        }
        
        return result;
    }
};