class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int n = arr.size();
        int totalSum = 0;
        
        for (int i = 0; i < n; ++i) {
            int endCount = i + 1;
            int startCount = n - i;
            int totalSubarrays = endCount * startCount;
            int oddSubarrays = (totalSubarrays + 1) / 2; // half of them are odd
            totalSum += oddSubarrays * arr[i];
        }
        
        return totalSum;
    }
};