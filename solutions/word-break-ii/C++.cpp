class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        unordered_map<string, vector<string>> memo;
        return backtrack(s, dict, memo);
    }
    
    vector<string> backtrack(string s, unordered_set<string>& dict, unordered_map<string, vector<string>>& memo) {
        if (memo.count(s)) return memo[s];
        if (s.empty()) return {""};
        
        vector<string> result;
        
        for (int len = 1; len <= s.size(); ++len) {
            string word = s.substr(0, len);
            if (dict.count(word)) {
                vector<string> rest = backtrack(s.substr(len), dict, memo);
                for (const string& sentence : rest) {
                    result.push_back(word + (sentence.empty() ? "" : " ") + sentence);
                }
            }
        }
        
        memo[s] = result;
        return result;
    }
};