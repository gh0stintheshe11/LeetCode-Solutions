#include <stdio.h>
#include <stdlib.h>

// Comparison function for qsort
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int heightChecker(int* heights, int heightsSize) {
    // Create a copy of the heights array
    int* expected = (int*)malloc(heightsSize * sizeof(int));
    for (int i = 0; i < heightsSize; i++) {
        expected[i] = heights[i];
    }

    // Sort the expected array
    qsort(expected, heightsSize, sizeof(int), compare);

    // Count the number of indices where heights[i] != expected[i]
    int count = 0;
    for (int i = 0; i < heightsSize; i++) {
        if (heights[i] != expected[i]) {
            count++;
        }
    }

    // Free the allocated memory
    free(expected);

    return count;
}