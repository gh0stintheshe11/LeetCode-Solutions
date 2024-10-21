class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> result;
        string row1 = "qwertyuiop";
        string row2 = "asdfghjkl";
        string row3 = "zxcvbnm";
        
        unordered_set<char> set1(row1.begin(), row1.end());
        unordered_set<char> set2(row2.begin(), row2.end());
        unordered_set<char> set3(row3.begin(), row3.end());
        
        for (string word : words) {
            string lowercaseWord = word;
            for (char& c : lowercaseWord) {
                c = tolower(c);
            }
            
            if (all_of(lowercaseWord.begin(), lowercaseWord.end(), [&](char c) { return set1.count(c); }) ||
                all_of(lowercaseWord.begin(), lowercaseWord.end(), [&](char c) { return set2.count(c); }) ||
                all_of(lowercaseWord.begin(), lowercaseWord.end(), [&](char c) { return set3.count(c); })) {
                result.push_back(word);
            }
        }
        return result;
    }
};