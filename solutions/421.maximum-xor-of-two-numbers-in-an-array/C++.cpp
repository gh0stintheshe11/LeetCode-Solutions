class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int maxNum = 0, mask = 0;
        unordered_set<int> prefixes;
        
        for (int i = 31; i >= 0; --i) {
            mask |= (1 << i);
            prefixes.clear();
            for (int num : nums) {
                prefixes.insert(num & mask);
            }
            
            int candidate = maxNum | (1 << i);
            for (int prefix : prefixes) {
                if (prefixes.count(candidate ^ prefix)) {
                    maxNum = candidate;
                    break;
                }
            }
        }
        
        return maxNum;
    }
};