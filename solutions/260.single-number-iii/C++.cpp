class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long long xorAll = 0;
        for (int num : nums) {
            xorAll ^= (long long)num;
        }

        long long diffBit = xorAll & -xorAll;
        int first = 0, second = 0;

        for (int num : nums) {
            if ((num & diffBit) != 0) {
                first ^= num;
            } else {
                second ^= num;
            }
        }

        return {first, second};
    }
};