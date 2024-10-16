class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> res;
        unordered_map<string, int> word_map;
        
        // Fill the word map with reversed words
        for (int i = 0; i < words.size(); ++i) {
            string reversed_word = words[i];
            reverse(reversed_word.begin(), reversed_word.end());
            word_map[reversed_word] = i;
        }

        for (int i = 0; i < words.size(); ++i) {
            string cur_word = words[i];
            int cur_len = cur_word.length();
            
            for (int j = 0; j <= cur_len; ++j) {
                string left = cur_word.substr(0, j);
                string right = cur_word.substr(j);
                
                // If left is a palindrome, check if there is a reversed right in the map
                if (isPalindrome(left)) {
                    if (word_map.find(right) != word_map.end() && word_map[right] != i) {
                        res.push_back({word_map[right], i});
                    }
                }
                
                // If right is a palindrome, check if there is a reversed left in the map
                if (j != cur_len && isPalindrome(right)) {
                    if (word_map.find(left) != word_map.end() && word_map[left] != i) {
                        res.push_back({i, word_map[left]});
                    }
                }
            }
        }
        
        return res;
    }
    
    bool isPalindrome(const string& str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str[left++] != str[right--]) {
                return false;
            }
        }
        return true;
    }
};