#include <stdio.h>
#include <stdlib.h>

// Function to remove the nth node from the end of the list
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Create a dummy node to handle edge cases such as removing the head
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    
    // Initialize two pointers, both starting at the dummy node
    struct ListNode* first = dummy;
    struct ListNode* second = dummy;
    
    // Move the first pointer n+1 steps ahead
    for (int i = 0; i <= n; i++) {
        first = first->next;
    }
    
    // Move both pointers until the first pointer reaches the end
    while (first != NULL) {
        first = first->next;
        second = second->next;
    }
    
    // Remove the nth node from the end
    struct ListNode* nodeToRemove = second->next;
    second->next = second->next->next;
    
    // Free the memory of the removed node
    free(nodeToRemove);
    
    // Get the new head of the list
    struct ListNode* newHead = dummy->next;
    
    // Free the dummy node
    free(dummy);
    
    return newHead;
}

// Helper function to create a new node
struct ListNode* createNode(int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

// Helper function to print the linked list
void printList(struct ListNode* head) {
    struct ListNode* current = head;
    while (current != NULL) {
        printf("%d ", current->val);
        current = current->next;
    }
    printf("\n");
}

// Helper function to free the linked list
void freeList(struct ListNode* head) {
    struct ListNode* current = head;
    while (current != NULL) {
        struct ListNode* next = current->next;
        free(current);
        current = next;
    }
}
