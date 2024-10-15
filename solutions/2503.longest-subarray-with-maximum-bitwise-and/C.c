int longestSubarray(int* nums, int numsSize) {
    // Step 1: Find the maximum element in the array
    int max_val = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > max_val) {
            max_val = nums[i];
        }
    }

    // Step 2: Find the longest subarray where elements are equal to max_val
    int max_length = 0;
    int current_length = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == max_val) {
            // Extend the current subarray length
            current_length++;
        } else {
            // Reset current subarray length and update max_length
            if (current_length > max_length) {
                max_length = current_length;
            }
            current_length = 0;
        }
    }

    // Handle the case where the last subarray is the longest
    if (current_length > max_length) {
        max_length = current_length;
    }

    return max_length;
}