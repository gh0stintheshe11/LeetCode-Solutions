class Solution {
public:
    bool isHappy(int n) {
        auto getNext = [](int number) {
            int totalSum = 0;
            while (number > 0) {
                int digit = number % 10;
                totalSum += digit * digit;
                number /= 10;
            }
            return totalSum;
        };

        int slow = n;
        int fast = getNext(n);
        
        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }

        return fast == 1;
    }
};