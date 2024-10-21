#include <stdio.h>

int removeElement(int* nums, int numsSize, int val) {
    int k = 0; // This will be the index for the next position to place a non-val element

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
}