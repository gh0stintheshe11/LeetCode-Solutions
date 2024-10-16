class MinStack {
private:
    std::vector<int> stack;
    std::vector<int> minStack;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        stack.push_back(val);
        if (minStack.empty() || val <= minStack.back()) {
            minStack.push_back(val);
        }
    }
    
    void pop() {
        if (stack.back() == minStack.back()) {
            minStack.pop_back();
        }
        stack.pop_back();
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return minStack.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */