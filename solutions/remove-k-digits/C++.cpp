class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k == num.length()) return "0";
        
        std::vector<char> stack;
        for (char c : num) {
            while (!stack.empty() && k > 0 && stack.back() > c) {
                stack.pop_back();
                k--;
            }
            stack.push_back(c);
        }

        // If k is still greater than 0, remove the remaining digits from the end
        while (k > 0) {
            stack.pop_back();
            k--;
        }
        
        // Construct the final number while removing leading zeros
        std::string result;
        bool leadingZero = true;
        for (char c : stack) {
            if (leadingZero && c == '0') continue;
            leadingZero = false;
            result.push_back(c);
        }

        return result.empty() ? "0" : result;
    }
};