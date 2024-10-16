class Solution {
public:
    string reverseWords(string s) {
        // First, we will use a two-pointer approach to reverse the entire string
        auto reverse = [](string& str, int start, int end) {
            while (start < end) {
                swap(str[start++], str[end--]);
            }
        };
        
        // Trim leading and trailing spaces
        int n = s.length();
        int start = 0, end = n - 1;
        while (start <= end && s[start] == ' ') start++;
        while (end >= start && s[end] == ' ') end--;
        
        // Reverse the entire trimmed string
        reverse(s, start, end);
        
        // Reverse each word in the reversed string
        int wordStart = -1;
        for (int i = start; i <= end; ++i) {
            if (s[i] != ' ' && wordStart == -1) {
                wordStart = i;  // Mark the start of a word
            } 
            else if (s[i] == ' ' && wordStart != -1) {
                reverse(s, wordStart, i - 1);
                wordStart = -1; // Reset word start marker
            }
        }
        
        // Reverse the last word if there is one
        if (wordStart != -1) {
            reverse(s, wordStart, end);
        }
        
        // Finally, construct the final result with a single space between words
        string result;
        bool isFirstWord = true;
        
        for (int i = start; i <= end; i++) {
            if (s[i] != ' ') {
                if (!isFirstWord) {
                    result += ' ';
                }
                while (i <= end && s[i] != ' ') {
                    result += s[i++];
                }
                isFirstWord = false;
            }
        }
        
        return result;
    }
};