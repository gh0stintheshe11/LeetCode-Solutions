int firstMissingPositive(int* nums, int numsSize) {
    int i = 0;

    while (i < numsSize) {
        // The value nums[i] should be placed at index nums[i] - 1
        // We need to ensure:
        // - nums[i] is in the range [1, numsSize]
        // - nums[i] != nums[nums[i] - 1] to avoid infinite swapping when duplicates exist
        if (nums[i] >= 1 && nums[i] <= numsSize && nums[nums[i] - 1] != nums[i]) {
            // Swap nums[i] with nums[nums[i] - 1]
            int temp = nums[nums[i] - 1];
            nums[nums[i] - 1] = nums[i];
            nums[i] = temp;
        } else {
            i++;
        }
    }

    // After rearrangement, the array should have nums[i] == i + 1
    for (i = 0; i < numsSize; i++) {
        if (nums[i] != i + 1) {
            // Found the first index where nums[i] != i + 1
            return i + 1;
        }
    }

    // All positions are filled correctly, so the missing number is numsSize + 1
    return numsSize + 1;
}
