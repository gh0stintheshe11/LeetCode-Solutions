#include <unordered_map>
#include <list>

class LRUCache {
private:
    int capacity;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cacheMap;
    std::list<std::pair<int, int>> cacheList;
    
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        auto it = cacheMap.find(key);
        if (it == cacheMap.end()) {
            return -1;
        }
        
        cacheList.splice(cacheList.begin(), cacheList, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = cacheMap.find(key);
        if (it != cacheMap.end()) {
            cacheList.splice(cacheList.begin(), cacheList, it->second);
            it->second->second = value;
            return;
        }
        
        if (cacheList.size() == capacity) {
            int lruKey = cacheList.back().first;
            cacheList.pop_back();
            cacheMap.erase(lruKey);
        }
        
        cacheList.emplace_front(key, value);
        cacheMap[key] = cacheList.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */