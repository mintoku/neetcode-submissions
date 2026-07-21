#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        std::string cleaned;
        for (char c : s) {
            if (std::isalnum(static_cast<unsigned char>(c))) {
                cleaned.push_back(std::tolower(static_cast<unsigned char>(c)));
            }
        }

        char* beginPointer = cleaned.data();
        char* endPointer = cleaned.data() + cleaned.size()-1;

        while (beginPointer < endPointer) {
            if (*beginPointer != *endPointer) {
                return false;
            }
            beginPointer++;
            endPointer--;
        }
        return true;
    }
};
