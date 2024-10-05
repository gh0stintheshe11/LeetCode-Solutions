#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int convertToMinutes(char* time) {
    int hours = (time[0] - '0') * 10 + (time[1] - '0');  
    int minutes = (time[3] - '0') * 10 + (time[4] - '0');
    return hours * 60 + minutes;
}

int cmp(const void* a, const void* b) {
    return (*(int*)a) - (*(int*)b);
}

int findMinDifference(char** timePoints, int timePointsSize) {
    if (timePointsSize < 2) return 0;

    int timeInMinutes[timePointsSize];
    for (int i = 0; i < timePointsSize; ++i) {
        timeInMinutes[i] = convertToMinutes(timePoints[i]);
    }

    qsort(timeInMinutes, timePointsSize, sizeof(int), cmp);

    int minDiff = 1440; // Maximum possible difference
    for (int i = 0; i < timePointsSize - 1; ++i) {
        int diff = timeInMinutes[i + 1] - timeInMinutes[i];
        if (diff < minDiff) {
            minDiff = diff;
        }
    }

    // Check the difference across midnight
    int acrossMidnightDiff = timeInMinutes[0] + 1440 - timeInMinutes[timePointsSize - 1];
    if (acrossMidnightDiff < minDiff) {
        minDiff = acrossMidnightDiff;
    }

    return minDiff;
}