class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> index(128, -1); // Initialize a list to store the last index of each character
        int maxLength = 0, start = 0; // maxLength keeps track of the longest length, start keeps track of the start of the current substring
        
        for (int i = 0; i < s.size(); i++) {
            if (index[s[i]] >= start) { // If the char was seen after or at the start
                start = index[s[i]] + 1; // Move the start to one past the last position of current char
            }
            index[s[i]] = i; // Update the last seen index of the current char
            maxLength = max(maxLength, i - start + 1); // Update the maxLength if the current length is greater
        }
        
        return maxLength; // Return the length of the longest substring found
    }
};