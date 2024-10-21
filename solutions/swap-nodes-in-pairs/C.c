#include <stdio.h>
#include <stdlib.h>

struct ListNode* swapPairs(struct ListNode* head) {
    // Create a dummy node to handle edge cases easily
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode* prev = &dummy;
    
    while (prev->next != NULL && prev->next->next != NULL) {
        // Nodes to be swapped
        struct ListNode* first = prev->next;
        struct ListNode* second = first->next;
        
        // Swapping
        first->next = second->next;
        second->next = first;
        prev->next = second;
        
        // Move prev two nodes ahead
        prev = first;
    }
    
    return dummy.next;
}

// Helper function to create a new ListNode
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
