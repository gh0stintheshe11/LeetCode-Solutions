class PeekingIterator : public Iterator {
private:
    int nextElement;
    bool hasNextElement;

public:
    PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        if (Iterator::hasNext()) {
            hasNextElement = true;
            nextElement = Iterator::next();
        } else {
            hasNextElement = false;
        }
    }
	
    int peek() {
        return nextElement;
    }
	
    int next() {
        int currentElement = nextElement;
        if (Iterator::hasNext()) {
            nextElement = Iterator::next();
        } else {
            hasNextElement = false;
        }
        return currentElement;
    }
	
    bool hasNext() const {
        return hasNextElement;
    }
};