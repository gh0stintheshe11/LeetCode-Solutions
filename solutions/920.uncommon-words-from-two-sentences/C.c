#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_WORD_LENGTH 100
#define MAX_WORDS 400

typedef struct {
    char word[MAX_WORD_LENGTH];
    int count;
} WordCount;

char** uncommonFromSentences(char* s1, char* s2, int* returnSize) {
    WordCount wordCounts[MAX_WORDS];
    int wordCountSize = 0;
    
    // Helper function to add or update word count
    void addWord(char* word) {
        for (int i = 0; i < wordCountSize; i++) {
            if (strcmp(wordCounts[i].word, word) == 0) {
                wordCounts[i].count++;
                return;
            }
        }
        strcpy(wordCounts[wordCountSize].word, word);
        wordCounts[wordCountSize].count = 1;
        wordCountSize++;
    }
    
    // Tokenize and count words in s1
    char* token = strtok(s1, " ");
    while (token != NULL) {
        addWord(token);
        token = strtok(NULL, " ");
    }
    
    // Tokenize and count words in s2
    token = strtok(s2, " ");
    while (token != NULL) {
        addWord(token);
        token = strtok(NULL, " ");
    }
    
    // Collect uncommon words
    char** result = (char**)malloc(MAX_WORDS * sizeof(char*));
    int resultSize = 0;
    for (int i = 0; i < wordCountSize; i++) {
        if (wordCounts[i].count == 1) {
            result[resultSize] = (char*)malloc((strlen(wordCounts[i].word) + 1) * sizeof(char));
            strcpy(result[resultSize], wordCounts[i].word);
            resultSize++;
        }
    }
    
    *returnSize = resultSize;
    return result;
}
