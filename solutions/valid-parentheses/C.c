#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

// Define a stack structure
typedef struct {
    char *data;
    int top;
    int capacity;
} Stack;

// Function to create a stack
Stack* createStack(int capacity) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->data = (char*)malloc(capacity * sizeof(char));
    return stack;
}

// Function to push an element onto the stack
void push(Stack *stack, char ch) {
    stack->data[++stack->top] = ch;
}

// Function to pop an element from the stack
char pop(Stack *stack) {
    if (stack->top == -1) {
        return '\0'; // Return null character if stack is empty
    }
    return stack->data[stack->top--];
}

// Function to check if the stack is empty
bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Function to check if the input string has valid parentheses
bool isValid(char* s) {
    int length = strlen(s);
    Stack *stack = createStack(length);
    
    for (int i = 0; i < length; i++) {
        char ch = s[i];
        if (ch == '(' || ch == '{' || ch == '[') {
            push(stack, ch);
        } else {
            char top = pop(stack);
            if ((ch == ')' && top != '(') ||
                (ch == '}' && top != '{') ||
                (ch == ']' && top != '[')) {
                free(stack->data);
                free(stack);
                return false;
            }
        }
    }
    
    bool result = isEmpty(stack);
    free(stack->data);
    free(stack);
    return result;
}