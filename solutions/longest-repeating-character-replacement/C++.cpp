class Solution {
public:
    int characterReplacement(string s, int k) {
        int maxCount = 0, maxLength = 0;
        int left = 0;
        int count[26] = {0};

        for (int right = 0; right < s.size(); ++right) {
            maxCount = max(maxCount, ++count[s[right] - 'A']);
            while (right - left + 1 - maxCount > k) {
                count[s[left] - 'A']--;
                left++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};