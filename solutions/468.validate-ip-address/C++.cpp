#include <string>
using namespace std;

class Solution {
public:
    string validIPAddress(string queryIP) {
        if (isValidIPv4(queryIP)) return "IPv4";
        if (isValidIPv6(queryIP)) return "IPv6";
        return "Neither";
    }

private:
    bool isValidIPv4(const string& ip) {
        int n = ip.size();
        if (count(ip.begin(), ip.end(), '.') != 3) return false;

        int start = 0, end;
        for (int i = 0; i < 4; ++i) {
            end = ip.find('.', start);
            if (end == string::npos) end = n;
            string block = ip.substr(start, end - start);
            if (block.empty() || block.size() > 3) return false;
            if (block[0] == '0' && block.size() > 1) return false;
            for (char c : block) {
                if (!isdigit(c)) return false;
            }
            int num = stoi(block);
            if (num < 0 || num > 255) return false;
            start = end + 1;
        }
        return true;
    }

    bool isValidIPv6(const string& ip) {
        int n = ip.size();
        if (count(ip.begin(), ip.end(), ':') != 7) return false;

        int start = 0, end;
        for (int i = 0; i < 8; ++i) {
            end = ip.find(':', start);
            if (end == string::npos) end = n;
            string block = ip.substr(start, end - start);
            if (block.empty() || block.size() > 4) return false;
            for (char c : block) {
                if (!isxdigit(c)) return false;
            }
            start = end + 1;
        }
        return true;
    }
};