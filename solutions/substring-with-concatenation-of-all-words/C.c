#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#define MAX_WORDS 5000     // Maximum number of words
#define MAX_WORD_LEN 30    // Maximum length of a word
#define HASH_MAP_SIZE 10007 // Size of the hash map

// Structure for hash map entry
typedef struct HashEntry {
    char* word;
    int index; // Unique index for the word
    struct HashEntry* next;
} HashEntry;

// Hash map for words
HashEntry* hashMap[HASH_MAP_SIZE];

// Hash function for strings
unsigned int hash(const char* str) {
    unsigned int h = 0;
    while (*str)
        h = h * 31 + (*str++);
    return h % HASH_MAP_SIZE;
}

// Insert word into hash map and assign an index
void insertWord(const char* word, int index) {
    unsigned int h = hash(word);
    HashEntry* entry = (HashEntry*)malloc(sizeof(HashEntry));
    entry->word = (char*)word; // We assume words are persistent (from words array)
    entry->index = index;
    entry->next = hashMap[h];
    hashMap[h] = entry;
}

// Search for a word in the hash map, return its index, or -1 if not found
int getWordIndex(const char* word) {
    unsigned int h = hash(word);
    HashEntry* entry = hashMap[h];
    while (entry != NULL) {
        if (strcmp(entry->word, word) == 0)
            return entry->index;
        entry = entry->next;
    }
    return -1; // Not found
}

// Free the hash map
void freeHashMap() {
    for (int i = 0; i < HASH_MAP_SIZE; i++) {
        HashEntry* entry = hashMap[i];
        while (entry != NULL) {
            HashEntry* temp = entry;
            entry = entry->next;
            free(temp);
        }
        hashMap[i] = NULL;
    }
}

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    int* result = NULL;
    *returnSize = 0;

    if (s == NULL || words == NULL || wordsSize == 0)
        return result;

    int sLen = strlen(s);
    int wordLen = strlen(words[0]);
    int totalLen = wordLen * wordsSize;

    if (sLen < totalLen)
        return result;

    // Step 1: Build the word index mapping and expected counts
    memset(hashMap, 0, sizeof(hashMap));

    int wordCount = 0; // Number of unique words
    int expectedCount[MAX_WORDS]; // Expected counts of words by index
    memset(expectedCount, 0, sizeof(expectedCount));

    for (int i = 0; i < wordsSize; i++) {
        int index = getWordIndex(words[i]);
        if (index == -1) {
            // New unique word
            insertWord(words[i], wordCount);
            expectedCount[wordCount]++;
            wordCount++;
        } else {
            expectedCount[index]++;
        }
    }

    // Allocate maximum possible result array
    result = (int*)malloc(sizeof(int) * (sLen - totalLen + 1));

    // Step 2: Slide the window
    for (int i = 0; i < wordLen; i++) {
        int left = i;
        int count = 0;
        int currentCount[MAX_WORDS];
        memset(currentCount, 0, sizeof(currentCount));

        for (int j = i; j <= sLen - wordLen; j += wordLen) {
            char* sub = s + j;

            // Extract the word
            char temp = sub[wordLen]; // Temporarily null-terminate the substring
            sub[wordLen] = '\0';
            int index = getWordIndex(sub);
            sub[wordLen] = temp; // Restore original character

            if (index != -1) {
                currentCount[index]++;
                count++;

                // If word count exceeds expected, adjust the window
                while (currentCount[index] > expectedCount[index]) {
                    // Remove the leftmost word
                    char* leftWord = s + left;
                    temp = leftWord[wordLen];
                    leftWord[wordLen] = '\0';
                    int leftIndex = getWordIndex(leftWord);
                    leftWord[wordLen] = temp;
                    currentCount[leftIndex]--;
                    count--;
                    left += wordLen;
                }

                // If all words matched
                if (count == wordsSize) {
                    result[*returnSize] = left;
                    (*returnSize)++;
                    // Move left to start searching for new window
                    // Remove the leftmost word
                    char* leftWord = s + left;
                    temp = leftWord[wordLen];
                    leftWord[wordLen] = '\0';
                    int leftIndex = getWordIndex(leftWord);
                    leftWord[wordLen] = temp;
                    currentCount[leftIndex]--;
                    count--;
                    left += wordLen;
                }
            } else {
                // Word not in words list, reset counts
                memset(currentCount, 0, sizeof(currentCount));
                count = 0;
                left = j + wordLen;
            }
        }
    }

    // Resize the result array to the actual number of results
    result = (int*)realloc(result, sizeof(int) * (*returnSize));

    // Free the hash map
    freeHashMap();

    return result;
}
