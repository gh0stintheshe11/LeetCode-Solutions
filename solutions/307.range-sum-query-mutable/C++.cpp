#include <vector>

using namespace std;

class NumArray {
    vector<int> BIT;
    vector<int> nums;
    int n;

    void updateBIT(int index, int delta) {
        for (int i = index; i <= n; i += (i & -i)) {
            BIT[i] += delta;
        }
    }

    int queryBIT(int index) {
        int sum = 0;
        for (int i = index; i > 0; i -= (i & -i)) {
            sum += BIT[i];
        }
        return sum;
    }

public:
    NumArray(vector<int>& nums) : nums(nums) {
        n = nums.size();
        BIT.resize(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            updateBIT(i + 1, nums[i]);
        }
    }

    void update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        updateBIT(index + 1, delta);
    }

    int sumRange(int left, int right) {
        return queryBIT(right + 1) - queryBIT(left);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */