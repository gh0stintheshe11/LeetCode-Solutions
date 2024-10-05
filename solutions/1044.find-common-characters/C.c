#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define ALPHABET_SIZE 26

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char **commonChars(char **words, int wordsSize, int* returnSize) {
    // Initialize the minimum frequency array with maximum possible values
    int minFreq[ALPHABET_SIZE];
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        minFreq[i] = INT_MAX;
    }

    // Update the minimum frequency array based on each word
    for (int i = 0; i < wordsSize; i++) {
        int charCount[ALPHABET_SIZE] = {0};
        for (int j = 0; words[i][j] != '\0'; j++) {
            charCount[words[i][j] - 'a']++;
        }
        for (int k = 0; k < ALPHABET_SIZE; k++) {
            if (charCount[k] < minFreq[k]) {
                minFreq[k] = charCount[k];
            }
        }
    }

    // Collect the common characters
    char **result = (char **)malloc(100 * sizeof(char *));
    *returnSize = 0;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        while (minFreq[i] > 0) {
            result[*returnSize] = (char *)malloc(2 * sizeof(char));
            result[*returnSize][0] = 'a' + i;
            result[*returnSize][1] = '\0';
            (*returnSize)++;
            minFreq[i]--;
        }
    }

    return result;
}