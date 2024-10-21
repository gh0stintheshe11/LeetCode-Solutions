class Solution {
public:
    string reverseVowels(string s) {
        int left = 0, right = s.size() - 1;
        auto isVowel = [](char c) {
            c = tolower(c);
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };

        while (left < right) {
            while (left < right && !isVowel(s[left])) {
                left++;
            }
            while (left < right && !isVowel(s[right])) {
                right--;
            }
            if (left < right) {
                std::swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
    }
};