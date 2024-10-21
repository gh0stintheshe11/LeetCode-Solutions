class Solution {
public:
    bool wordPattern(string pattern, string s) {
        // Split the string `s` into words
        vector<string> words;
        stringstream ss(s);
        string word;
        while (ss >> word) {
            words.push_back(word);
        }
        
        // If the number of pattern characters doesn't match the number of words
        if (pattern.size() != words.size()) {
            return false;
        }
        
        unordered_map<char, string> charToWordMap;
        unordered_map<string, char> wordToCharMap;
        
        for (int i = 0; i < pattern.size(); ++i) {
            char c = pattern[i];
            const string& w = words[i];
            
            if (charToWordMap.count(c) && charToWordMap[c] != w) {
                return false;
            }
            if (wordToCharMap.count(w) && wordToCharMap[w] != c) {
                return false;
            }
            
            charToWordMap[c] = w;
            wordToCharMap[w] = c;
        }
        
        return true;
    }
};