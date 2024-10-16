class Solution {
public:
    int magicalString(int n) {
        if (n <= 0) return 0;
        if (n <= 3) return 1;
        
        std::string s = "122";
        int count = 1; // As there is one '1' initially
        int i = 2;
        
        while (s.size() < n) {
            int num = s.back() == '1' ? 2 : 1;
            int times = s[i] - '0';
            s.append(times, num + '0');
            if (num == 1) count += std::min(times, n - static_cast<int>(s.size()) + times);
            i++;
        }
        
        return count;
    }
};