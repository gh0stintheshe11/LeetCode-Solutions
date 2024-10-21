class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> mappings = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> result;

        function<void(int, string&)> backtrack = [&](int index, string& path) {
            if (index == digits.size()) {
                result.push_back(path);
                return;
            }
            int digit = digits[index] - '0';
            for (char letter : mappings[digit]) {
                path.push_back(letter);
                backtrack(index + 1, path);
                path.pop_back();
            }
        };

        string currentPath;
        backtrack(0, currentPath);
        return result;
    }
};