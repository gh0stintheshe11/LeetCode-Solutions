/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;
        
        ListNode *slow = head, *fast = head, *prev = nullptr, *temp = nullptr;
        
        // Find the mid-point using the slow and fast pointers
        while (fast && fast->next) {
            fast = fast->next->next;
            temp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = temp;
        }
        
        // For odd number of nodes, move slow one step further
        if (fast) {
            slow = slow->next;
        }
        
        // Compare the reversed first half with the second half
        while (prev && slow) {
            if (prev->val != slow->val)
                return false;
            prev = prev->next;
            slow = slow->next;
        }
        
        return true;
    }
};