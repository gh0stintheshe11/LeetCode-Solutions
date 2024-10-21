class Solution {
public:
    bool isValidSerialization(string preorder) {
        int slots = 1; // Start with one available slot for the root
        int n = preorder.size();
        
        for (int i = 0; i < n; ++i) {
            if (preorder[i] == ',') {
                continue;
            }
            
            // Decrement slots for current node visit
            if (--slots < 0) {
                return false;
            }

            // If not a number, move i to the end of the current number
            if (preorder[i] != '#') {
                // A non-null node creates two additional slots
                slots += 2;
                // Skip the number entirely
                while (i < n && preorder[i] != ',') {
                    ++i;
                }
            }
        }
        
        return slots == 0;
    }
};