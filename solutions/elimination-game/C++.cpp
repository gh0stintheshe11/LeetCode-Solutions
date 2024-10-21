class Solution {
public:
    int lastRemaining(int n) {
        bool leftToRight = true;
        int remaining = n, step = 1, head = 1;
        
        while (remaining > 1) {
            if (leftToRight || remaining % 2 == 1) {
                head += step;
            }
            remaining /= 2;
            step *= 2;
            leftToRight = !leftToRight;
        }
        
        return head;
    }
};