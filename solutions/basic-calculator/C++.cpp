class Solution {
public:
    int calculate(string s) {
        int n = s.size();
        stack<int> ops;
        ops.push(1);
        int sign = 1;

        int i = 0;
        int result = 0;
        while (i < n) {
            char c = s[i];
            if (isdigit(c)) {
                int num = 0;
                while (i < n && isdigit(s[i])) {
                    num = num * 10 + (s[i] - '0');
                    i++;
                }
                result += sign * num;
                continue;
            } else if (c == '+') {
                sign = ops.top();
            } else if (c == '-') {
                sign = -ops.top();
            } else if (c == '(') {
                ops.push(sign);
            } else if (c == ')') {
                ops.pop();
            }
            i++;
        }
        
        return result;
    }
};