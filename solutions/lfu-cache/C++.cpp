#include <unordered_map>
#include <list>

class LFUCache {
public:
    LFUCache(int capacity) : capacity(capacity), minFreq(0) {}

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        updateFreq(key);
        return cache[key].first;
    }

    void put(int key, int value) {
        if (capacity == 0) return;

        // If key exists, update its value and frequency
        if (cache.find(key) != cache.end()) {
            cache[key].first = value;
            updateFreq(key);
            return;
        }

        // If at capacity, remove the least frequently used element
        if (cache.size() == capacity) {
            int keyToRemove = freqListMap[minFreq].back();
            freqListMap[minFreq].pop_back();
            if (freqListMap[minFreq].empty()) freqListMap.erase(minFreq);
            cache.erase(keyToRemove);
        }

        // Add new key
        cache[key] = {value, 1};
        freqListMap[1].push_front(key);
        keyIterator[key] = freqListMap[1].begin();
        minFreq = 1;
    }

private:
    int capacity;
    int minFreq;
    std::unordered_map<int, std::pair<int, int>> cache; // key -> {value, freq}
    std::unordered_map<int, std::list<int>> freqListMap; // freq -> list of keys
    std::unordered_map<int, std::list<int>::iterator> keyIterator; // key -> its position in the list

    void updateFreq(int key) {
        int freq = cache[key].second;
        freqListMap[freq].erase(keyIterator[key]);
        if (freqListMap[freq].empty()) {
            freqListMap.erase(freq);
            if (minFreq == freq) ++minFreq;
        }
        cache[key].second++;
        freqListMap[freq + 1].push_front(key);
        keyIterator[key] = freqListMap[freq + 1].begin();
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */