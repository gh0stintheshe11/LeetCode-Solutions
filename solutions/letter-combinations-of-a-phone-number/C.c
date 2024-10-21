#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Mapping of digits to letters
const char* mappings[] = {
    "",     // 0
    "",     // 1
    "abc",  // 2
    "def",  // 3
    "ghi",  // 4
    "jkl",  // 5
    "mno",  // 6
    "pqrs", // 7
    "tuv",  // 8
    "wxyz"  // 9
};

// Helper function for backtracking
void backtrack(char** result, int* returnSize, char* digits, char* current, int index, int digitsLen) {
    // If the current combination is complete, add it to the result
    if (index == digitsLen) {
        result[*returnSize] = strdup(current);
        (*returnSize)++;
        return;
    }
    
    // Get the corresponding letters for the current digit
    const char* letters = mappings[digits[index] - '0'];
    
    // Iterate over the possible letters for this digit
    for (int i = 0; letters[i] != '\0'; i++) {
        current[index] = letters[i];
        backtrack(result, returnSize, digits, current, index + 1, digitsLen);
    }
}

char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    
    // Edge case: If digits is empty, return an empty array
    if (digits[0] == '\0') {
        return NULL;
    }
    
    // Calculate the total number of combinations
    int maxCombinations = 1;
    int digitsLen = strlen(digits);
    for (int i = 0; i < digitsLen; i++) {
        maxCombinations *= strlen(mappings[digits[i] - '0']);
    }
    
    // Allocate memory for the result
    char** result = (char**)malloc(maxCombinations * sizeof(char*));
    char* current = (char*)malloc((digitsLen + 1) * sizeof(char));
    current[digitsLen] = '\0';  // Null-terminate the current combination string
    
    // Start the backtracking process
    backtrack(result, returnSize, digits, current, 0, digitsLen);
    
    free(current);
    return result;
}