#include <unordered_map>
using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> count;
        for (char c : s) {
            count[c]++;
        }
        
        int length = 0;
        bool hasOdd = false;
        for (auto& pair : count) {
            if (pair.second % 2 == 0) {
                length += pair.second;
            } else {
                length += pair.second - 1;
                hasOdd = true;
            }
        }
        
        if (hasOdd) {
            length++;
        }
        
        return length;
    }
};