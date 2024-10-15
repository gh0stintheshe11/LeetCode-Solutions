/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Helper function to reverse a portion of the linked list
struct ListNode* reverse(struct ListNode* head, int k) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next = NULL;
    
    while (k > 0) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        k--;
    }
    
    return prev; // The new head after reversal
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode* curr = head;
    int count = 0;

    // First, check if there are at least k nodes left in the linked list
    while (curr != NULL && count < k) {
        curr = curr->next;
        count++;
    }

    // If we have at least k nodes, we reverse the first k nodes
    if (count == k) {
        // Reverse the first k nodes
        struct ListNode* newHead = reverse(head, k);
        
        // Now head is the last node in the reversed group, we recursively reverse the remaining list
        head->next = reverseKGroup(curr, k);
        
        return newHead;
    }

    // If we don't have k nodes, return head (remaining nodes as is)
    return head;
}