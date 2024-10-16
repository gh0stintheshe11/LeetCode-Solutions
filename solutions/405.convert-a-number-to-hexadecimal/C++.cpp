class Solution {
public:
    string toHex(int num) {
        if (num == 0) return "0";
        unsigned int n = num;
        string hex = "";
        char hexChars[] = "0123456789abcdef";
        while (n != 0) {
            hex = hexChars[n & 0xf] + hex;
            n >>= 4;
        }
        return hex;
    }
};