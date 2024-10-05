#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Comparison function for qsort
int compare(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    // Initialize return size
    *returnSize = 0;

    // Edge case: if the array size is less than 4, no quadruplets can be found
    if (numsSize < 4) {
        return NULL;
    }

    // Sort the array to apply two-pointer technique
    qsort(nums, numsSize, sizeof(int), compare);

    // Allocate initial memory for result and column sizes
    int capacity = 1000;  // Initial capacity
    int** result = (int**)malloc(capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity * sizeof(int));

    // Iterate through the array to fix the first two elements
    for (int i = 0; i < numsSize - 3; i++) {
        // Skip duplicates for the first element
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        for (int j = i + 1; j < numsSize - 2; j++) {
            // Skip duplicates for the second element
            if (j > i + 1 && nums[j] == nums[j - 1]) {
                continue;
            }

            // Use two pointers to find the remaining two elements
            int left = j + 1;
            int right = numsSize - 1;

            while (left < right) {
                long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];

                if (sum == target) {
                    // Check if we need to resize the result array
                    if (*returnSize == capacity) {
                        capacity *= 2;
                        result = (int**)realloc(result, capacity * sizeof(int*));
                        *returnColumnSizes = (int*)realloc(*returnColumnSizes, capacity * sizeof(int));
                    }

                    // Allocate space for the quadruplet
                    result[*returnSize] = (int*)malloc(4 * sizeof(int));
                    result[*returnSize][0] = nums[i];
                    result[*returnSize][1] = nums[j];
                    result[*returnSize][2] = nums[left];
                    result[*returnSize][3] = nums[right];
                    (*returnColumnSizes)[*returnSize] = 4;
                    (*returnSize)++;

                    // Move the pointers and skip duplicates
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return result;
}