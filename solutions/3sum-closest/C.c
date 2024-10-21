#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Comparison function for qsort
int compare(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

int threeSumClosest(int* nums, int numsSize, int target) {
    // Step 1: Sort the array
    qsort(nums, numsSize, sizeof(int), compare);

    int closestSum = nums[0] + nums[1] + nums[2];  // Initialize with the first three elements

    // Step 2: Iterate through the array
    for (int i = 0; i < numsSize - 2; i++) {
        int left = i + 1;
        int right = numsSize - 1;

        // Step 3: Use two-pointer technique to find the closest sum
        while (left < right) {
            int currentSum = nums[i] + nums[left] + nums[right];

            // If the current sum is exactly the target, return immediately
            if (currentSum == target) {
                return currentSum;
            }

            // Update the closest sum if the current one is closer to the target
            if (abs(currentSum - target) < abs(closestSum - target)) {
                closestSum = currentSum;
            }

            // Move the pointers
            if (currentSum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    return closestSum;
}