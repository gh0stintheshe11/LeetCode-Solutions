#include <string>
#include <unordered_map>
#include <cmath>

class Solution {
public:
    std::string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        
        std::string result;
        
        // Determine the sign
        if ((numerator < 0) ^ (denominator < 0)) result += "-";
        
        // Convert to long to handle overflow cases
        long long num = std::labs(numerator);
        long long denom = std::labs(denominator);
        
        // Integral part
        result += std::to_string(num / denom);
        num %= denom;
        
        if (num == 0) return result;
        
        // Fractional part
        result += ".";
        std::unordered_map<long long, int> remainderIndexMap;
        
        while (num != 0) {
            if (remainderIndexMap.find(num) != remainderIndexMap.end()) {
                result.insert(remainderIndexMap[num], "(");
                result += ")";
                break;
            }
            
            remainderIndexMap[num] = result.size();
            num *= 10;
            result += std::to_string(num / denom);
            num %= denom;
        }
        
        return result;
    }
};