#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cstdlib>

class RandomizedCollection {
public:
    RandomizedCollection() {
    }
    
    bool insert(int val) {
        elements.push_back(val);
        indices[val].insert(elements.size() - 1);
        return indices[val].size() == 1;
    }
    
    bool remove(int val) {
        if (indices[val].empty()) return false;
        
        int indexToRemove = *indices[val].begin();
        indices[val].erase(indexToRemove);
        
        int lastElement = elements.back();
        elements[indexToRemove] = lastElement;

        indices[lastElement].erase(elements.size() - 1);
        if (indexToRemove < elements.size() - 1) {
            indices[lastElement].insert(indexToRemove);
        }

        elements.pop_back();
        
        return true;
    }
    
    int getRandom() {
        return elements[rand() % elements.size()];
    }
    
private:
    std::vector<int> elements;
    std::unordered_map<int, std::unordered_set<int>> indices;
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */