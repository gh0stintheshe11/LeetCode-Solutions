#include <vector>
#include <unordered_map>
#include <cstdlib>

class RandomizedSet {
private:
    std::vector<int> nums;
    std::unordered_map<int, int> numIndices;

public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (numIndices.find(val) != numIndices.end()) {
            return false;
        }
        nums.push_back(val);
        numIndices[val] = nums.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (numIndices.find(val) == numIndices.end()) {
            return false;
        }
        int lastElement = nums.back();
        numIndices[lastElement] = numIndices[val];
        nums[numIndices[val]] = lastElement;
        nums.pop_back();
        numIndices.erase(val);
        return true;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */