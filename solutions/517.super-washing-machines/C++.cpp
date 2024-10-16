class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int total = accumulate(machines.begin(), machines.end(), 0);
        int n = machines.size();
        if (total % n != 0) return -1;
        int target = total / n;
        
        int maxMoves = 0, prefixSum = 0;
        for (int dresses : machines) {
            int diff = dresses - target;
            prefixSum += diff;
            maxMoves = max(maxMoves, max(abs(prefixSum), diff));
        }
        
        return maxMoves;
    }
};