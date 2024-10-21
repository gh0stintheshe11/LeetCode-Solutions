#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int longestValidParentheses(char* s) {
    int maxLen = 0;
    int length = strlen(s);
    if (length == 0)
        return 0;

    // Stack to store indices
    int* stack = (int*)malloc(sizeof(int) * (length + 1));
    int top = -1;

    // Initialize the stack with -1
    stack[++top] = -1;

    for (int i = 0; i < length; i++) {
        if (s[i] == '(') {
            // Push the index of '(' onto the stack
            stack[++top] = i;
        } else {
            // Pop the top element (matching '(' or the initial -1)
            top--;

            if (top == -1) {
                // Stack is empty, push the current index as a new base
                stack[++top] = i;
            } else {
                // Calculate the length of the current valid substring
                int currentLen = i - stack[top];
                if (currentLen > maxLen)
                    maxLen = currentLen;
            }
        }
    }

    free(stack); // Free the allocated memory
    return maxLen;
}
