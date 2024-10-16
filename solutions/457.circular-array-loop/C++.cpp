class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        int n = nums.size();
        
        auto getIndex = [&](int i) {
            return ((i + nums[i]) % n + n) % n; // handle negative modulo
        };
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) continue;
            
            int slow = i, fast = i;
            int direction = nums[i];
            
            while (true) {
                slow = getIndex(slow);
                if (nums[slow] * direction <= 0) break;
                
                fast = getIndex(fast);
                if (nums[fast] * direction <= 0) break;
                fast = getIndex(fast);
                if (nums[fast] * direction <= 0) break;
                
                if (slow == fast) {
                    if (slow == getIndex(slow)) break;
                    return true;
                }
            }
            
            slow = i;
            int val = nums[i];
            while (nums[slow] * val > 0) {
                int next = getIndex(slow);
                nums[slow] = 0;
                slow = next;
            }
        }
        
        return false;
    }
};