/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
private:
    vector<int> flatList;
    int index;

    void flatten(const vector<NestedInteger> &nestedList) {
        for (const auto &ni : nestedList) {
            if (ni.isInteger()) {
                flatList.push_back(ni.getInteger());
            } else {
                flatten(ni.getList());
            }
        }
    }
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) : index(0) {
        flatten(nestedList);
    }
    
    int next() {
        return flatList[index++];
    }
    
    bool hasNext() {
        return index < flatList.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */