#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Comparator function to use in qsort
int compare(const void *a, const void *b) {
    char ab[22], ba[22];
    sprintf(ab, "%d%d", *(int*)a, *(int*)b);
    sprintf(ba, "%d%d", *(int*)b, *(int*)a);
    return strcmp(ba, ab); // Sort in descending order
}

char* largestNumber(int* nums, int numsSize) {
    if (numsSize == 0) return "";

    // Sort the array with the custom comparator
    qsort(nums, numsSize, sizeof(int), compare);

    // Calculate the total length of the result string
    int totalLength = 0;
    for (int i = 0; i < numsSize; i++) {
        totalLength += snprintf(NULL, 0, "%d", nums[i]);
    }

    // Allocate memory for the result string
    char *result = (char*)malloc(totalLength + 1);
    result[0] = '\0';

    // Concatenate sorted numbers into the result string
    for (int i = 0; i < numsSize; i++) {
        char buffer[12];
        sprintf(buffer, "%d", nums[i]);
        strcat(result, buffer);
    }

    // Handle the case where the result is "0" (e.g., [0, 0])
    if (result[0] == '0') {
        result[1] = '\0';
    }

    return result;
}