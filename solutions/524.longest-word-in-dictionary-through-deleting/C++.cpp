class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        string longestWord = "";
        
        for (const string& word : dictionary) {
            int i = 0;
            for (char c : s) {
                if (i < word.length() && word[i] == c) {
                    i++;
                }
            }
            if (i == word.length()) { // word is a subsequence of s
                if (word.length() > longestWord.length() || 
                    (word.length() == longestWord.length() && word < longestWord)) {
                    longestWord = word;
                }
            }
        }
        
        return longestWord;
    }
};