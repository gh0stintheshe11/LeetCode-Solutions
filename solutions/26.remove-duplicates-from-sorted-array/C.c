#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int j = 0; // Pointer for the position of the last unique element

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[j]) {
            j++;
            nums[j] = nums[i];
        }
    }

    return j + 1; // The number of unique elements
}
