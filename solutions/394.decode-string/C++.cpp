class Solution {
public:
    string decodeString(string s) {
        stack<int> counts;
        stack<string> resultStack;
        string current = "";
        int index = 0;
        while (index < s.length()) {
            if (isdigit(s[index])) {
                int count = 0;
                while (isdigit(s[index])) {
                    count = count * 10 + (s[index] - '0');
                    index++;
                }
                counts.push(count);
            } else if (s[index] == '[') {
                resultStack.push(current);
                current = "";
                index++;
            } else if (s[index] == ']') {
                string temp = resultStack.top(); resultStack.pop();
                int repeatTimes = counts.top(); counts.pop();
                for (int i = 0; i < repeatTimes; i++) {
                    temp += current;
                }
                current = temp;
                index++;
            } else {
                current += s[index];
                index++;
            }
        }
        return current;
    }
};