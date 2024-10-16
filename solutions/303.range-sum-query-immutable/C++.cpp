class NumArray {
    vector<int> prefixSum;
public:
    NumArray(vector<int>& nums) {
        prefixSum.resize(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); ++i) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return prefixSum[right + 1] - prefixSum[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */