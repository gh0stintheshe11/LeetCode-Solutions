class Solution {
public:
    int calculate(string s) {
        int n = s.size();
        int currentNumber = 0, lastNumber = 0, result = 0;
        char operation = '+';
        
        for (int i = 0; i < n; ++i) {
            if (isdigit(s[i])) {
                currentNumber = currentNumber * 10 + (s[i] - '0');
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == n - 1) {
                if (operation == '+' || operation == '-') {
                    result += lastNumber;
                    lastNumber = (operation == '+') ? currentNumber : -currentNumber;
                } else if (operation == '*') {
                    lastNumber *= currentNumber;
                } else if (operation == '/') {
                    lastNumber /= currentNumber;
                }
                operation = s[i];
                currentNumber = 0;
            }
        }
        result += lastNumber;
        return result;
    }
};