#include <stdlib.h>

int trap(int* height, int heightSize) {
    if (heightSize <= 2)
        return 0;

    int* left_max = (int*)malloc(sizeof(int) * heightSize);
    int* right_max = (int*)malloc(sizeof(int) * heightSize);
    int water_trapped = 0;

    // Precompute left_max array
    left_max[0] = height[0];
    for (int i = 1; i < heightSize; i++) {
        left_max[i] = (height[i] > left_max[i - 1]) ? height[i] : left_max[i - 1];
    }

    // Precompute right_max array
    right_max[heightSize - 1] = height[heightSize - 1];
    for (int i = heightSize - 2; i >= 0; i--) {
        right_max[i] = (height[i] > right_max[i + 1]) ? height[i] : right_max[i + 1];
    }

    // Calculate trapped water
    for (int i = 0; i < heightSize; i++) {
        int min_height = (left_max[i] < right_max[i]) ? left_max[i] : right_max[i];
        water_trapped += (min_height > height[i]) ? min_height - height[i] : 0;
    }

    free(left_max);
    free(right_max);
    return water_trapped;
}

