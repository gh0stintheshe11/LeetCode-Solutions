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
#include <cstdlib>

class Solution {
public:
    ListNode* head;
    
    Solution(ListNode* head) {
        this->head = head;
    }
    
    int getRandom() {
        int result, index = 1;
        ListNode* curr = head;
        while (curr != nullptr) {
            if (rand() % index == 0) {
                result = curr->val;
            }
            index++;
            curr = curr->next;
        }
        return result;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */