#include <vector>
#include <algorithm>
#include <random>

class Solution {
public:
    Solution(std::vector<int>& nums) : original(nums), current(nums) {
        std::random_device rd;
        rng = std::mt19937(rd());
    }
    
    std::vector<int> reset() {
        current = original;
        return current;
    }
    
    std::vector<int> shuffle() {
        std::shuffle(current.begin(), current.end(), rng);
        return current;
    }
    
private:
    std::vector<int> original;
    std::vector<int> current;
    std::mt19937 rng;
};