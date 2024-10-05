class Solution {
public:
    void reverseWords(vector<char>& s) {
        // Helper function to reverse a portion of the array
        auto reverse = [](vector<char>& s, int left, int right) {
            while (left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        };

        int n = s.size();

        // Step 1: reverse the entire array
        reverse(s, 0, n - 1);

        // Step 2: reverse each word in the reversed array
        int start = 0;
        for (int end = 0; end < n; ++end) {
            if (s[end] == ' ') {
                reverse(s, start, end - 1);
                start = end + 1;
            }
        }
        // Reverse the last word
        reverse(s, start, n - 1);
    }
};