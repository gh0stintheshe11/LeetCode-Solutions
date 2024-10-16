class Solution {
public:
    string getPermutation(int n, int k) {
        string result;
        string numbers = "123456789";
        vector<int> factorial(n, 1);
        
        for (int i = 1; i < n; ++i) {
            factorial[i] = factorial[i - 1] * i;
        }
        
        --k; // convert k to zero-indexed
        
        for (int i = n; i > 0; --i) {
            int index = k / factorial[i - 1];
            result += numbers[index];
            numbers.erase(index, 1);
            k %= factorial[i - 1];
        }
        
        return result;
    }
};