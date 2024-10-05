#include <limits.h>  // For INT_MAX and INT_MIN

double findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {
    // Ensure nums1 is the smaller array
    if (m > n) {
        // Swap nums1 and nums2
        int* tempNums = nums1;
        nums1 = nums2;
        nums2 = tempNums;

        // Swap m and n
        int tempLen = m;
        m = n;
        n = tempLen;
    }

    int low = 0, high = m, halfLen = (m + n + 1) / 2;
    while (low <= high) {
        int i = (low + high) / 2;
        int j = halfLen - i;

        int nums1LeftMax = (i == 0) ? INT_MIN : nums1[i - 1];
        int nums1RightMin = (i == m) ? INT_MAX : nums1[i];

        int nums2LeftMax = (j == 0) ? INT_MIN : nums2[j - 1];
        int nums2RightMin = (j == n) ? INT_MAX : nums2[j];

        if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
            // Correct partition found
            int maxLeft = (nums1LeftMax > nums2LeftMax) ? nums1LeftMax : nums2LeftMax;
            int minRight = (nums1RightMin < nums2RightMin) ? nums1RightMin : nums2RightMin;

            if ((m + n) % 2 == 1) {
                // Odd total length
                return maxLeft;
            } else {
                // Even total length
                return ((maxLeft + minRight) / 2.0);
            }
        } else if (nums1LeftMax > nums2RightMin) {
            // Move partition in nums1 to the left
            high = i - 1;
        } else {
            // Move partition in nums1 to the right
            low = i + 1;
        }
    }

    // If we reach here, the arrays are not sorted or the input is invalid
    return 0.0;
}
