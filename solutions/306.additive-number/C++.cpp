class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        for (int i = 1; i <= n / 2; ++i) {
            for (int j = 1; j <= (n - i) / 2; ++j) {
                if (check(num, i, j)) return true;
            }
        }
        return false;
    }

private:
    bool check(const string &num, int i, int j) {
        if (num[0] == '0' && i > 1) return false;
        if (num[i] == '0' && j > 1) return false;
        long long num1 = stoll(num.substr(0, i));
        long long num2 = stoll(num.substr(i, j));
        string sum;
        for (int start = i + j; start != num.size(); start += sum.size()) {
            num2 = num1 + num2;
            num1 = num2 - num1;
            sum = to_string(num2);
            if (num.substr(start).find(sum) != 0) return false;
        }
        return true;
    }
};