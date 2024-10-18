#include <stdio.h>
#include <stdlib.h>

// Comparator function to sort the slots based on start time
int compare_slots(const void* a, const void* b) {
    int* slotA = *(int**)a;
    int* slotB = *(int**)b;
    if (slotA[0] < slotB[0]) return -1;
    else if (slotA[0] > slotB[0]) return 1;
    else return 0;
}

int* minAvailableDuration(int** slots1, int slots1Size, int* slots1ColSize, 
                         int** slots2, int slots2Size, int* slots2ColSize, 
                         int duration, int* returnSize) {
    // Sort both slots1 and slots2 based on start time
    qsort(slots1, slots1Size, sizeof(int*), compare_slots);
    qsort(slots2, slots2Size, sizeof(int*), compare_slots);
    
    int i = 0, j = 0;
    *returnSize = 0;
    int* result = NULL;
    
    // Traverse both lists to find the earliest overlapping slot
    while (i < slots1Size && j < slots2Size) {
        int start_overlap = slots1[i][0] > slots2[j][0] ? slots1[i][0] : slots2[j][0];
        int end_overlap = slots1[i][1] < slots2[j][1] ? slots1[i][1] : slots2[j][1];
        
        // Check if the overlapping duration is sufficient
        if (end_overlap - start_overlap >= duration) {
            result = (int*)malloc(2 * sizeof(int));
            result[0] = start_overlap;
            result[1] = start_overlap + duration;
            *returnSize = 2;
            return result;
        }
        
        // Move the pointer that has the earlier end time
        if (slots1[i][1] < slots2[j][1]) {
            i++;
        } else {
            j++;
        }
    }
    
    // If no suitable slot is found, return an empty array
    return result;
}