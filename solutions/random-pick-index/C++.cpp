class Solution {
private:
    std::unordered_map<int, std::vector<int>> indices_map;
    
public:
    Solution(std::vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            indices_map[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        const auto& indices = indices_map[target];
        int random_index = rand() % indices.size();
        return indices[random_index];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */